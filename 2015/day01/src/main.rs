use std::io::prelude::BufRead;
use std::io::BufReader;
use std::fs::File;

const FILENAME: &str = "input";

fn main() {
    let f = File::open(FILENAME).expect("FRIGGGGGGGGGGGGG");
    let reader = BufReader::new(f);

    let mut iterator = 0;
    let mut basement = 0;
    let mut flip  = false;

    for line in reader.lines() {
        for c in line.expect("I HATE RUST").chars() {
            if c == '(' {
                iterator += 1;
            } else if c == ')' {
                iterator -= 1;
            }
            if iterator >= 0 && !flip {
                basement += 1;
            } else if !flip {
                basement += 1;
                flip = !flip;
            }
        }
    }
    println!("Floor: {iterator}");
    println!("Basement: {basement}");
}