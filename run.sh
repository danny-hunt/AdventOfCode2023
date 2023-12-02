# Take single number argument and set it as an environment variable for the rest of the commands
export DAY=$1

python3 python/main.py 
(cd rust; DAY=$1 RUST_BACKTRACE=1 cargo run)

