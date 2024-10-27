# file_writer.py
import os

def write_to_file(filename, content):
    """Writes the provided content to the specified file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")

def main():
    """Main function to handle the file writing."""
    filename = '/home/pi/output.txt'
    content = "Hello, this is a test content!"
    write_to_file(filename, content)

if __name__ == '__main__':
    main()
