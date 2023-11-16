import unittest
import subprocess
import os
import logging
logger = logging.getLogger(__name__)

class TestYourProgram(unittest.TestCase):
    def test_end_to_end(self):
        for i in range(1,6):
            logger.debug(f"TC #{i} >> -----------------------------")
            input_file = f'sample_input/input{i}.txt'
            actual_output_file = f'generated_output/output{i}.txt'
            expected_output_file = f'sample_output/output{i}.txt'
            
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(actual_output_file), exist_ok=True)

            # Run your program with the sample input and capture standard output
            result = subprocess.run(['python3', '-m', 'geektrust', input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Write the standard output to the actual output file
            with open(actual_output_file, 'w') as output_file:
                output_file.write(result.stdout)

            with open(actual_output_file, 'r') as file1, open(expected_output_file, 'r') as file2:
                lines_file1 = file1.readlines()
                lines_file2 = file2.readlines()
                for lineIdx in range(0,len(lines_file1)):
                    line1 = lines_file1[lineIdx].replace("\n","")
                    line2 = lines_file2[lineIdx].replace("\n","")
                    logger.debug(f"TC #{i} Actual")
                    logger.debug(line1)
                    
                    logger.debug(f"TC #{i} Expected")
                    logger.debug(line2)
                    self.assertEqual(line1,line2)
            
if __name__ == '__main__':
    unittest.main()