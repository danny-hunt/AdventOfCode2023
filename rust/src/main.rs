use once_cell::sync::Lazy;
use regex::Regex;
use std::{env, process::Command};

static MS_REGEX: Lazy<Regex> = Lazy::new(|| Regex::new(r"Time: (\d+)ms").unwrap());

fn extract_time(s: &str) -> u32 {
    let capture = MS_REGEX.captures_iter(s).next().unwrap();
    capture[1].parse().unwrap()
}

fn main() {
    let day = env::var("DAY")
        .unwrap_or("25".to_string())
        .parse::<i32>()
        .unwrap();
    let total_time = (1..=day)
        .map(|day_num| {
            let day = format!("{:0>2}", day_num);
            let cmd = Command::new("cargo")
                .args(["run", "--release", "--bin", &day])
                .output()
                .unwrap();
            let output = String::from_utf8(cmd.stdout).unwrap();
            println!("Day {}:\n{}", day, output);

            extract_time(&output)
        })
        .sum::<u32>();
    println!("Total time: {}ms", total_time);
}
