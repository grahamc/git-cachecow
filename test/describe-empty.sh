#!/bin/bash

cd sub_1
../../git-submodule-describe > ../submodule-describe-empty.output

cd ..
diff submodule-describe-empty.output submodule-describe-empty.expected

exit $?

