# Take single number argument and set it as an environment variable for the rest of the commands
export DAY=$1

python3 python/main.py 
(cd rust; DAY=$1 RUST_BACKTRACE=1 cargo run)

# For each subdirectory in ./go, run the main.go file
for dir in ./go/*/; do
    (cd "$dir" && DAY=$1 go run main.go)
done

