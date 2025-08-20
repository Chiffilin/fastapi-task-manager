# For see all this list of commands run:
# ```bash
# just --list
# ```
# All docs is only "one-liner".
#
# Plugin: https://plugins.jetbrains.com/plugin/18658-just
#

import 'just/dev.just'
import 'just/app.just'

# List of all commands
[private]
@default:
    just --list --justfile {{ justfile() }}

# [other]-[BEGIN]
# https://youtu.be/ZXsQAXx_ao0?si=CMMwwtkaWoaGjUTg

# You can!
@do-it:
    echo "Make your dreams come true"

# [other]-[END]
