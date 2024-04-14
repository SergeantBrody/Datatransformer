from reader import CSVReader, JSONReader, TXTReader, PickleReader, CSVWriter, JSONWriter, TXTWriter, PickleWriter, \
    DataTransformer
import sys

if len(sys.argv) < 4:
    print("Insufficient arguments. Provide input filename, output filename, and changes.")


else:

    def load_arguments():
        return sys.argv[1], sys.argv[2], sys.argv[3:]


    input_filename, output_filename, changes = load_arguments()

    file_extension_input = input_filename.split('.')[-1]
    file_extension_output = output_filename.split('.')[-1]

    if file_extension_input == 'csv':
        reader = CSVReader(input_filename)
        input_format = 'csv'
    elif file_extension_input == 'json':
        reader = JSONReader(input_filename)
        input_format = 'json'
    elif file_extension_input == 'txt':
        reader = TXTReader(input_filename)
        input_format = 'txt'
    elif file_extension_input == 'pkl':
        reader = PickleReader(input_filename)
        input_format = 'pkl'
    else:
        print("Unsupported input file format.")

    if file_extension_output == 'csv':
        writer = CSVWriter(output_filename)
    elif file_extension_output == 'json':
        writer = JSONWriter(output_filename)
    elif file_extension_output == 'txt':
        writer = TXTWriter(output_filename)
    elif file_extension_output == 'pkl':
        writer = PickleWriter(output_filename)
    else:
        print("Unsupported output file format.")

data = reader.read()
transformer = DataTransformer(data, changes, input_format)
transformer.modify()
transformer.display()
writer.write(data)
