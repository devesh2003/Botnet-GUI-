import Home
import Control

def main():
    home_page = Home.HomePage()
    home_page.start()

    if home_page.status:
        cmd_control = Control.CommandAndControl()
        cmd_control.start()

if __name__ == '__main__':
    main()