use itertools::Itertools;
use std::path::Path;
use std::{error::Error, fs, process::Command};

fn extract_microseconds(output: &str) -> Result<usize, Box<dyn Error>> {
    let out = output.lines().last().unwrap();
    let time = if out.ends_with("ms") {
        out["Time: ".len()..out.len() - 2].parse::<usize>()? * 1000
    } else {
        out["Time: ".len()..out.len() - 3].parse::<usize>()?
    };
    Ok(time)
}

fn main() -> Result<(), Box<dyn Error>> {
    let toml_path = Path::new(env!("CARGO_MANIFEST_DIR"));

    let path = toml_path.parent().unwrap();

    let days = fs::read_dir(path.join("rust/src/bin"))?
        .filter_map(|p| p.ok()?.path().file_stem()?.to_str().map(str::to_string))
        .sorted()
        .collect::<Vec<_>>();
    println!(env!("CARGO_MANIFEST_DIR"));
    let mut total_time = 0;
    for day in &days {
        println!("Running day {}...", day);
        let cmd = Command::new("cargo").args(["run", "--release", "--bin", day]);

        println!("cmd {:?}", cmd);
        // .output()?;
        let output: String = String::from_utf8(cmd.output()?.stdout)?;
        println!("Day {}:\n{}", day, output);
        total_time += extract_microseconds(&output)?;
    }
    println!("Total time: {}ms", total_time / 1000);
    Ok(())
}
