echo ""
echo ""
echo -e "\e[97m>>> Enter The URL You Want To Mask...\n\e[96m"
      read -p " Target > " url
      content=$(curl -s "$url")
      node app.js --url $url
