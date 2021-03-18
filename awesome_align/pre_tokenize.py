import argparse
import random
import itertools
import os
import tempfile
import warnings
warnings.filterwarnings("ignore")

from awesome_align.tokenization_bert import BasicTokenizer

def main():
  parser = argparse.ArgumentParser()
  
  parser.add_argument(
        "--data_file", default=None, type=str, required=True, help="The input data file (a text file)."
    )
  
  file_path=args.data_file
  
  # Default Arguments for Cased Multlingual
  tokenizer = BasicTokenizer()
  
  assert os.path.isfile(file_path)
  print('Loading the dataset...')
  self.examples = []
  with open(file_path, encoding="utf-8") as f:
      for idx, line in enumerate(f.readlines()):
          if len(line) == 0 or line.isspace() or not len(line.split(' ||| ')) == 2:
              raise ValueError(f'Line {idx+1} is not in the correct format!')

          src, tgt = line.split(' ||| ')
          if src.rstrip() == '' or tgt.rstrip() == '':
              raise ValueError(f'Line {idx+1} is not in the correct format!')

          sent_src, sent_tgt = src.strip() , tgt.strip()
          token_src, token_tgt = tokenizer.tokenize(sent_src) , tokenizer.tokenize(sent_tgt)
          token_src_string, token_tgt_string = ' '.join([t for t in token_src]) , ' '.join([t for t in token_tgt])
          
          print(token_src_string + ' ||| ' + token_tgt_string)

if __name__ == "__main__":
    main()
