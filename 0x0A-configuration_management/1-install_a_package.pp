#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
ensure   => '2.1.0',
provider => 'pip3'
}
# Install an especific version of Werkzeug (2.1.1)
package {'Werkzeug':
ensure   =>  '2.1.1',
provider => 'pip3'
}
