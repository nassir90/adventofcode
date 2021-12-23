use std::fs;
use std::cmp::{min,max};

#[derive(Copy)]
#[derive(Clone)]
struct Range (i64,i64,i64,i64,i64,i64);

fn clamp_range(slave: &Range, master: &Range) -> Range {
    let &Range(xmin1, xmax1, ymin1, ymax1, zmin1, zmax1) = slave;
    let &Range(xmin2, xmax2, ymin2, ymax2, zmin2, zmax2) = master;
    Range(
        clamp(xmin1, xmin2, xmax2),
        clamp(xmax1, xmin2, xmax2),
        clamp(ymin1, ymin2, ymax2),
        clamp(ymax1, ymin2, ymax2),
        clamp(zmin1, zmin2, zmax2),
        clamp(zmax1, zmin2, zmax2)
    )
}

fn clamp(number: i64, minimum: i64, maximum: i64) -> i64 {
    max(minimum, min(number, maximum))
}
fn get_volume(r: &Range) -> i64 {
    ((r.1 - r.0) * (r.3 - r.2) * (r.5 - r.4)).abs()
}

fn main() {
    let mut input = fs::read_to_string("input").unwrap();
    let mut commands = Vec::new();
    for line in input.lines() {
        let mut components : Vec<_> = line.split_whitespace().collect();
        let value = components[0];
        let components : Vec<&str> = components[1].split(",").collect();
        let x_range : Vec<i64> = components[0][2..].split("..").map(|elem| elem.parse().unwrap()).collect();
        let y_range : Vec<i64> = components[1][2..].split("..").map(|elem| elem.parse().unwrap()).collect();
        let z_range : Vec<i64> = components[2][2..].split("..").map(|elem| elem.parse().unwrap()).collect();
        commands.push((value, Range(x_range[0], x_range[1], y_range[0], y_range[1], z_range[0], z_range[1])));
    }

    let mut ranges = Vec::new();
    for (command, command_range) in commands {
        let mut new_ranges = Vec::new();
        for range in ranges.iter() {
            let &Range(xmin2, xmax2, ymin2, ymax2, zmin2, zmax2) = range;
            let Range(xmin, xmax, ymin, ymax, zmin, zmax) = clamp_range(&command_range, range);
            let top = Range(xmin2, xmax2, ymin2, ymax2, zmax, zmax2);
            let bottom = Range(xmin2, xmax2, ymin2, ymax2, zmin2, zmin);
            let left = Range(xmin2, xmin, ymin2, ymax2, zmin, zmax);
            let right = Range(xmax, xmax2, ymin2, ymax2, zmin, zmax);
            let front = Range(xmin, xmax, ymin2, ymin, zmin, zmax);
            let back = Range(xmin, xmax, ymax, ymax2, zmin, zmax);
            let parts = [top, bottom, left, right, front, back];
            let volume : i64 = parts.iter().map(|part| get_volume(part)).sum();
            if volume != 0 {
                if volume == get_volume(range) {
                    new_ranges.push(*range);
                } else {
                    for part in parts.iter() {
                        new_ranges.push(*part);
                    }
                }
            }
        }
        ranges = new_ranges;

        if command == "on" {
            ranges.push(command_range)
        }
    }

    println!("{}", ranges.iter().map(|part| get_volume(part)).sum::<i64>());
}
