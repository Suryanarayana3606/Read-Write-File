def sort_and_write_names(input_file, output_file):

  try:
    with open(input_file, 'r') as f:
      names = f.read().splitlines()

    # Sort names alphabetically
    sorted_names = sorted(names, key=str.lower)  # Case-insensitive sorting

    with open(output_file, 'w') as f:
      for name in sorted_names:
        f.write(name + '\n')

    print("Names sorted and written to", output_file)

  except FileNotFoundError:
    print("Input file not found:", input_file)
  except IOError as e:
    print("Error writing to output file:", e)

input_file = 'unsorted_names.txt'
output_file = 'sorted_names.txt'
sort_and_write_names(input_file, output_file)
