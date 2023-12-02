struct CubeSet {
    red: u8,
    green: u8,
    blue: u8,
}

impl CubeSet {
    fn new(red: u8, green: u8, blue: u8) -> Self {
        Self { red, green, blue }
    }

    fn display(&self) -> String {
        format!("{} red, {} green, {} blue", self.red, self.green, self.blue)
    }
}

struct Game {
    id: u8,
    cubes: Vec<CubeSet>,
}

impl Game {
    fn new(id: u8, cubes: Vec<CubeSet>) -> Self {
        Self { id, cubes }
    }
}

fn line_parser(input: &str) -> Game {
    if input.is_empty() {
        panic!("input is empty");
    }
    let (game_string, trial_sets) = match input.split_once(": ") {
        Some(tuple) => tuple,
        None => panic!("input is not a game"),
    };
    let game_id = match game_string.split_once("Game ") {
        Some(tuple) => tuple.1.parse::<u8>().unwrap(),
        None => panic!("input is not a game"),
    };
    let trial_sets = trial_sets
        .split("; ")
        .map(|s| {
            let color_s = s.split(", ").collect::<Vec<&str>>();
            let mut red = 0;
            let mut green = 0;
            let mut blue = 0;
            for color in color_s {
                let (number_s, color_s) = color.split_once(' ').unwrap();
                let number = number_s.parse::<u8>().unwrap();
                match color_s {
                    "red" => red = number,
                    "green" => green = number,
                    "blue" => blue = number,
                    _ => panic!("input is not a color"),
                }
            }
            CubeSet::new(red, green, blue)
        })
        .collect::<Vec<CubeSet>>();
    Game::new(game_id, trial_sets)
}

fn game_power(game: &Game) -> u32 {
    // Find maximum for each color in the cube sets and multiply them together
    let mut red = 0;
    let mut green = 0;
    let mut blue = 0;
    for cube_set in &game.cubes {
        if cube_set.red > red {
            red = cube_set.red;
        }
        if cube_set.green > green {
            green = cube_set.green;
        }
        if cube_set.blue > blue {
            blue = cube_set.blue;
        }
    }
    red as u32 * green as u32 * blue as u32
}

fn game_valid(game: &Game) -> bool {
    let red_max = 12;
    let green_max = 13;
    let blue_max = 14;

    for cube_set in &game.cubes {
        if cube_set.red > red_max {
            return false;
        }
        if cube_set.green > green_max {
            return false;
        }
        if cube_set.blue > blue_max {
            return false;
        }
    }
    true
}

#[aoc::main(02)]
fn main(input: &str) -> (usize, usize) {
    let xs = input
        .lines()
        .map(|s: &str| line_parser(s))
        .fold(0, |acc: u16, game| {
            if game_valid(&game) {
                acc + game.id as u16
            } else {
                acc
            }
        });
    let p1 = xs.try_into().unwrap();

    let p2 = input
        .lines()
        .map(|s: &str| line_parser(s))
        .fold(0, |acc: u32, game| acc + game_power(&game))
        .try_into()
        .unwrap();
    (p1, p2)
}
