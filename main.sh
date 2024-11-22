#!/bin/bash

while true; do
    echo "Menu:"
    echo "1. Open the website"
    echo "2. Enter a word and store in log.txt"
    echo "3. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Opening the website..."
            python3 app.py &
            sleep 2
            xdg-open http://127.0.0.1:5000
            ;;
        2)
            read -p "Enter a word: " word
            echo "$word" >> log.txt
            echo "Word saved in log.txt."
            read -p "Do you want to open the website? (y/n): " open_website
            if [[ $open_website == "y" || $open_website == "Y" ]]; then
                echo "Opening the website..."
                python3 app.py &
                sleep 2
                xdg-open http://127.0.0.1:5000
            else
                echo "Exiting without opening the website."
            fi
            ;;
        3)
            echo "Exiting."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            ;;
    esac
done
