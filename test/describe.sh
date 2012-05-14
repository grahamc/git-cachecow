#!/bin/bash

git clone owner.git owner
cd owner
../../git-submodule-describe > ../submodule-describe.output

cd ..
diff submodule-describe.output submodule-describe.expected

exit $?

