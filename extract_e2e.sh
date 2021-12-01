INPUT=$1
OUTPUT="$1".pretok
python pre_tokenize.py --data_file $1 --output_file $OUTPUT

DATA_FILE=$OUTPUT
MODEL_NAME_OR_PATH=bert-base-multilingual-cased
OUTPUT_FILE="$OUTPUT".aligned

CUDA_VISIBLE_DEVICES=1 awesome-align \
    --output_file=$OUTPUT_FILE \
    --model_name_or_path=$MODEL_NAME_OR_PATH \
    --data_file=$DATA_FILE \
    --extraction 'softmax' \
    --batch_size 4 \
    --cache_dir .
