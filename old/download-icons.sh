#!/bin/bash

# Material Symbolsアイコンのリスト
icons=(
  "account_tree" "article" "attach_file" "auto_awesome" "bolt" "brush" "build"
  "business" "cable" "change_history" "chat" "check_circle" "close" "cloud"
  "cloud_upload" "code" "compare" "create_new_folder" "dashboard" "description"
  "download" "edit_note" "extension" "fact_check" "favorite" "feather" "flag"
  "folder" "folder_special" "format_quote" "forum" "groups" "help" "hourglass_top"
  "image" "inventory" "inventory_2" "language" "lightbulb" "link" "list_alt"
  "menu_book" "model_training" "movie" "palette" "payments" "play_circle"
  "psychology" "rate_review" "repeat" "rocket_launch" "savings" "school"
  "sentiment_dissatisfied" "settings" "smart_toy" "spa" "speed" "star" "storage"
  "summarize" "supervisor_account" "target" "terminal" "thumb_up" "timer" "tune"
  "view_list" "view_sidebar" "volunteer_activism" "warning" "schedule"
)

# 各アイコンをダウンロード
for icon in "${icons[@]}"; do
  echo "Downloading $icon..."
  # Material Symbols Outlined SVG from Google Fonts
  curl -s "https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/${icon}/default/48px.svg" \
    -o "icons/${icon}.svg"
  
  if [ ! -s "icons/${icon}.svg" ]; then
    echo "Failed to download $icon, trying alternative URL..."
    # Alternative: use Material Icons instead
    curl -s "https://raw.githubusercontent.com/google/material-design-icons/master/symbols/web/${icon}/materialsymbolsoutlined/24px.svg" \
      -o "icons/${icon}.svg"
  fi
done

echo "All icons downloaded to icons/ directory"
