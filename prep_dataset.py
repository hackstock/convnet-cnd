import os
import shutil

DATA = 'data'
CATS = 'cat'
DOGS = 'dog'
TRAIN = 'train'
VALIDATE = 'validate'
TEST = 'test'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, DATA)

TRAIN_DIR = os.path.join(BASE_DIR, TRAIN)
TRAIN_DIR_CATS = os.path.join(TRAIN_DIR, CATS)
TRAIN_DIR_DOGS = os.path.join(TRAIN_DIR, DOGS)

VALIDATE_DIR = os.path.join(BASE_DIR, VALIDATE)
VALIDATE_DIR_CATS = os.path.join(VALIDATE_DIR, CATS)
VALIDATE_DIR_DOGS = os.path.join(VALIDATE_DIR, DOGS)

TEST_DIR = os.path.join(BASE_DIR, TEST)
TEST_DIR_CATS = os.path.join(TEST_DIR, CATS)
TEST_DIR_DOGS = os.path.join(TEST_DIR, DOGS)

def make_directories():
    os.mkdir(TRAIN_DIR)
    os.mkdir(TRAIN_DIR_CATS)
    os.mkdir(TRAIN_DIR_DOGS)

    os.mkdir(VALIDATE_DIR)
    os.mkdir(VALIDATE_DIR_CATS)
    os.mkdir(VALIDATE_DIR_DOGS)

    os.mkdir(TEST_DIR)
    os.mkdir(TEST_DIR_CATS)
    os.mkdir(TEST_DIR_DOGS)

def generate_filenames(train_val_test_sizes, class_of_interest):
    train_size, val_size, test_size = train_val_test_sizes
    train_file_names = ["{}.{}.jpg".format(class_of_interest, i) for i in range(train_size)]
    val_file_names = ["{}.{}.jpg".format(class_of_interest, i) for i in range(train_size, train_size + val_size)]
    test_file_names = ["{}.{}.jpg".format(class_of_interest, i) for i in range(train_size + val_size, train_size + val_size + test_size)]

    return (train_file_names, val_file_names, test_file_names)

def copy_files(filenames, coi):
    train_fnames, val_fnames, test_fnames = filenames
    for fname in train_fnames:
        src = os.path.join(os.path.join(DATA_DIR,TRAIN),fname)
        dest = os.path.join(os.path.join(TRAIN_DIR,coi),fname)
        shutil.copyfile(src,dest)

    for fname in val_fnames:
        src = os.path.join(os.path.join(DATA_DIR,TRAIN),fname)
        dest = os.path.join(os.path.join(VALIDATE_DIR,coi),fname)
        shutil.copyfile(src,dest)

    for fname in test_fnames:
        src = os.path.join(os.path.join(DATA_DIR,TRAIN),fname)
        dest = os.path.join(os.path.join(TEST_DIR,coi),fname)
        shutil.copyfile(src,dest)

def main():
    make_directories()
    cat_filenames = generate_filenames((1000,500,500),"cat")
    copy_files(cat_filenames, "cat")

    dog_filenames = generate_filenames((1000,500,500),"dog")
    copy_files(dog_filenames, "dog")


if __name__ == '__main__':
    main()

   




