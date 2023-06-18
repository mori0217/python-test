from optparse import OptionGroup, OptionParser


def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action="store", type="string", dest='filename', help='File name')
    parser.add_option('-n', '--num', action="store", type="int", dest='num', help='Number')
    parser.set_defaults(verbose=False)
    parser.add_option('-v', '--verbose', action="store_true", dest='verbose', help='Verbose flag')
    parser.add_option('-q', '--quiet', action="store_false", dest='verbose', help='Quiet flag')
    parser.add_option('-r', action="store_const", const="root", dest='user_name', help='Root user name')

    parser.add_option("-e", dest="env")

    def is_release(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't release")
        setattr(parser.values, option.dest, True)
    parser.add_option("--release", action="callback", callback=is_release, dest="release")

    group = OptionGroup(parser, "Dangerous Options")
    group.add_option("-g", action="store_true", help="Group option")
    parser.add_option_group(group)

    options, args = parser.parse_args()
    print('options: ', options)
    print('args: ', args)


if __name__ == '__main__':
    main()
