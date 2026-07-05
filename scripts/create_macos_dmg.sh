#!/usr/bin/env bash
set -euo pipefail

APP_PATH="${1:-dist/StreamCap.app}"
DMG_PATH="${2:-dist/StreamCap-macos.dmg}"
VOLUME_NAME="${3:-StreamCap}"
BACKGROUND_IMAGE="${4:-assets/images/dmg.jpg}"

if [ ! -d "$APP_PATH" ]; then
  echo "App bundle not found: $APP_PATH" >&2
  exit 1
fi

if [ ! -f "$BACKGROUND_IMAGE" ]; then
  echo "DMG background image not found: $BACKGROUND_IMAGE" >&2
  exit 1
fi

WORK_DIR="$(mktemp -d)"
MOUNT_DIR="$WORK_DIR/mount"
RW_DMG="$WORK_DIR/$VOLUME_NAME-rw.dmg"
DEVICE=""

log() {
  echo "==> $*"
}

cleanup() {
  if [ -n "$DEVICE" ]; then
    hdiutil detach "$DEVICE" -quiet || true
  fi
  rm -rf "$WORK_DIR"
}
trap cleanup EXIT

mkdir -p "$MOUNT_DIR"

APP_SIZE_MB="$(du -sm "$APP_PATH" | awk '{print $1}')"
DMG_SIZE_MB="$((APP_SIZE_MB + 200))"

log "Creating writable DMG image (${DMG_SIZE_MB} MB)"
hdiutil create "$RW_DMG" \
  -volname "$VOLUME_NAME" \
  -size "${DMG_SIZE_MB}m" \
  -fs HFS+ \
  -format UDRW

log "Mounting writable DMG"
ATTACH_OUTPUT="$(hdiutil attach "$RW_DMG" -readwrite -noverify -noautoopen -mountpoint "$MOUNT_DIR")"
echo "$ATTACH_OUTPUT"
DEVICE="$(echo "$ATTACH_OUTPUT" | awk '/Apple_HFS/ {print $1; exit}')"
if [ -z "$DEVICE" ]; then
  echo "Could not determine mounted DMG device." >&2
  exit 1
fi

log "Copying app bundle and installer assets"
cp -R "$APP_PATH" "$MOUNT_DIR/"
ln -s /Applications "$MOUNT_DIR/Applications"
mkdir -p "$MOUNT_DIR/.background"
cp "$BACKGROUND_IMAGE" "$MOUNT_DIR/.background/background.jpg"

log "Configuring Finder window layout"
if ! osascript <<APPLESCRIPT
tell application "Finder"
  tell disk "$VOLUME_NAME"
    open
    set current view of container window to icon view
    set toolbar visible of container window to false
    set statusbar visible of container window to false
    set the bounds of container window to {100, 100, 930, 580}
    set viewOptions to the icon view options of container window
    set arrangement of viewOptions to not arranged
    set icon size of viewOptions to 96
    set background picture of viewOptions to file ".background:background.jpg"
    set position of item "StreamCap.app" of container window to {200, 250}
    set position of item "Applications" of container window to {630, 250}
    update without registering applications
    delay 2
    close
  end tell
end tell
APPLESCRIPT
then
  echo "Warning: Finder layout customization failed. The DMG will still include the app and Applications shortcut." >&2
fi

log "Detaching writable DMG"
hdiutil detach "$DEVICE" -quiet
DEVICE=""

log "Converting writable DMG to compressed image"
mkdir -p "$(dirname "$DMG_PATH")"
hdiutil convert "$RW_DMG" \
  -format UDZO \
  -imagekey zlib-level=9 \
  -o "$DMG_PATH" \
  -ov

echo "Created DMG: $DMG_PATH"
