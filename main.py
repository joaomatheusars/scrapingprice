from interface.gui import App
import os.path 

def main():
    if not os.path.exists('Sheets'):
        os.mkdir('Sheets')
    app = App() 
    
if __name__ == "__main__":
    main()