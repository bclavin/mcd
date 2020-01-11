if [ -d "/Users/" ]
then
  environment="Mac"
else
  environment="Linux"
fi

echo "Running on $environment"

if [ $environment == "Linux" ]
then
  chrome_version_cmd="google-chrome-stable --version"
else
  chrome_version_cmd="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version"
fi

chrome_version=$(eval $chrome_version_cmd)
string=${chrome_version#*Google Chrome }
echo "$string"

end=${string##*.}
echo "Last . is in column $((${#string} - ${#end}))"

last_period_position=$((${#string} - ${#end}))

echo "last_period_position $last_period_position"

short_version=${string:0:$last_period_position-1}
echo "short_version $short_version"

latest_version_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$short_version"

echo "latest_version_url $latest_version_url"

#string="${string#foo}"
#echo "$string"

chrome_driver_version=$(eval curl $latest_version_url)
echo $chrome_driver_version
