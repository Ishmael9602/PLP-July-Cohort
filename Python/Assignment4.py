def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("✅ File read successfully.")

        # Modify content
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    print("📄 Welcome to the File Modifier Program!")
    input_filename = input("Enter the name of the file to read from: ").strip()
    output_filename = input("Enter the name of the file to write to: ").strip()

    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
