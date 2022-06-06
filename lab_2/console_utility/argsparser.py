import argparse


class ArgsParser:

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', dest="l_arg", nargs='+')
        parser.add_argument('-d', dest="d_arg", nargs='+')
        parser.add_argument('-c', dest="c_arg", nargs='?', default=None)
        return parser.parse_args()

    @staticmethod
    def load_from() -> list[str]:
        args = ArgsParser.parse()
        return args.l_arg

    @staticmethod
    def dump_in() -> list[str]:
        args = ArgsParser.parse()
        return args.d_arg

    @staticmethod
    def getargs():
        args = ArgsParser.parse()

        if args.c_arg is not None:
            args.l_arg, args.d_arg = ArgsParser.get_config(str(args.c_arg))

        return args.d_arg, args.l_arg

    @staticmethod
    def get_config(config: str) -> list[str]:
        try:
            file = open(config, "r")
            configs = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
            return configs.split("\n")
