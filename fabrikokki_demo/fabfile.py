# August 10, 2010 -- ss
#
#   Just getting it all to run, the main FabriKokki code pulls in
#   our provider replacements!
#
#   Not sure they're working yet...

from fabric.api import *

from fabrikokki import FabriKokki

def cook_fabric():
    print "Creating FabriKokki"
    fk = FabriKokki('config.yaml')

    print "Here's your FabriKokki"
    fk._print()

    print "Exiting!"
    sys.exit(1)

    # Haven't quite gotten this far, but works to here
    kokki.run_roles(['nginx_test'])
