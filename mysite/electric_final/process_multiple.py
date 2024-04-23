import os
from multiprocessing import Pool
import time


def process_file(file_name):
    print('Processing file', file_name)
    os.system(f"python3 main_final.py {file_name}")


def remove_symbols(input_string, symbols=(".pdf", ".", ":", "*", "?", '"', "<", ">", "/", "\\", "|", "-", '(', ')', '$', '&')):
    """The function removes symbols forbidden for naming"""

    for symbol in symbols:
        input_string = input_string.replace(symbol, "")
    input_string = input_string.strip().replace(' ', '_')
    input_string += '.pdf'
    return input_string


def main():
    t1 = time.perf_counter()

    resulting_folder = 'resulting_folder/'
    if not os.path.exists(resulting_folder):
        os.makedirs(resulting_folder)

    for filename in os.listdir('pdf_folder/'):
        try:
            old_name = f'pdf_folder/{filename}'
            new_name = f'pdf_folder/{remove_symbols(filename)}'
            os.rename(old_name, new_name)
            print(new_name, ' <-- new name')
        except:
            print(filename, 'file skipped')

    file_list = os.listdir('pdf_folder/')

    # Specify the number of concurrent processes (adjust as needed)
    num_processes = 3

    with Pool(processes=num_processes) as pool:
        pool.map(process_file, file_list)

    t2 = time.perf_counter()
    print(f'Total execution time for all files is: {t2 - t1}')


if __name__ == '__main__':
    main()

