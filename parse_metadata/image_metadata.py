import argparse
from PIL import Image
from PIL.ExifTags import TAGS


def get_metadata_from_image(image_name, output_image):
    """
    :param image_name: input file name
    :param output_image: outpute file name
    :return: image metadata tags
    """
    try:
        meta_data = {}
        img = Image.open(image_name)
        print('[+] Getting metadata')
        info = img._getexif()
        print('[+] getexif data')
        print(info)
        if info:
            print('[+] Found metadata from image')
            for (tag, value) in info.items():
                tag_name = TAGS.get(tag, tag)
                meta_data[tag_name] = value
                if not output_image:
                    print('Tagname: {} value: {}'.format(tag_name, value))
            if output_image:
                print('[+] Outputting to file')
                with open(output_image, 'w') as file:
                    for(tag_name, value) in meta_data.items():
                        file.write(str(tag_name) + '\t' + str(value) + '\n')
    except Exception as ex:
        print('Failed: {}'.format(ex))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', help='name of img file')
    parser.add_argument('-o', '--output', help='dump data out file')
    args = parser.parse_args()
    if args.img:
        get_metadata_from_image(args.img, args.output)
    else:
        print(parser.usage)


if __name__ == '__main__':
    main()