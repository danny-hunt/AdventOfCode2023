use aho_corasick::{AhoCorasick, Match};

fn first_and_last(input: &str) -> String {
    if input.is_empty() {
        panic!("input is empty");
    }

    let first_char = input.chars().next().unwrap();
    let last_char = input.chars().next_back().unwrap();

    format!("{}{}", first_char, last_char)
}

fn match_to_digit_string(input: &str) -> &str {
    match input {
        "zero" => "0",
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9",
        "0" => "0",
        "1" => "1",
        "2" => "2",
        "3" => "3",
        "4" => "4",
        "5" => "5",
        "6" => "6",
        "7" => "7",
        "8" => "8",
        "9" => "9",
        _ => panic!("input is not a digit"),
    }
}

#[aoc::main(01)]
fn main(input: &str) -> (usize, usize) {
    // println!("input:\n{}", input.get(0..200).unwrap_or_default());
    let xs = input
        .lines()
        .map(|s: &str| s.chars().filter(|c| c.is_ascii_digit()).collect::<String>())
        .map(|s: String| first_and_last(&s).parse::<u32>().unwrap())
        .sum::<u32>();
    let p1 = xs.try_into().unwrap();

    let number_strings = &[
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3",
        "4", "5", "6", "7", "8", "9",
    ];
    let ac: AhoCorasick = AhoCorasick::new(number_strings).unwrap();
    let xss = input
        .lines()
        .map(|s: &str| {
            ac.find_overlapping_iter(s)
                .map(|m: Match| match_to_digit_string(number_strings[m.pattern()]))
                .collect::<String>()
        })
        .map(|s: String| first_and_last(&s).parse::<u32>().unwrap())
        .sum::<u32>();

    let p2 = xss.try_into().unwrap();
    (p1, p2)
}
