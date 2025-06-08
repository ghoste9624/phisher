#!/bin/bash

# Function to display help information
show_help() {
  echo "Usage: $0 [URL]"
  echo "Shortens the given URL using the TinyURL API."
  echo "If no URL is provided, it reads the URL from standard input."
  echo ""
  echo "Example:"
  echo "  $0 https://www.example.com"
  echo "  echo https://www.example.com | $0"
}

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  # If no URL is provided, read from standard input
  read -p "Enter URL to shorten: " long_url
else
  # If a URL is provided, use it
  long_url="$1"
fi

# Check if the help flag is present
if [[ "$long_url" == "-h" || "$long_url" == "--help" ]]; then
  show_help
  exit 0
fi

# Use curl to call the TinyURL API
short_url=$(curl -s "https://tinyurl.com/api-create.php?url=$long_url")

# Check if the shortening was successful
if [ -z "$short_url" ]; then
  echo "Error: Failed to shorten URL."
  exit 1
fi

# Display the shortened URL
echo "Shortened URL: $short_url"
