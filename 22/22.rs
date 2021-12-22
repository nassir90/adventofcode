use std::fs;
use std::cmp::{min,max};

fn main() {
    let mut input = fs::read_to_string("input").unwrap();
    let mut commands = Vec::new();
    for line in input.lines() {
        let mut components : Vec<_> = line.split_whitespace().collect();
        let value : i32 = components[0].parse().unwrap();
        let x_range : Vec<i32> = components[1].split("..").map(|elem| elem.parse().unwrap()).collect();
        let y_range : Vec<i32> = components[2].split("..").map(|elem| elem.parse().unwrap()).collect();
        let z_range : Vec<i32> = components[3].split("..").map(|elem| elem.parse().unwrap()).collect();
        commands.push((value, (x_range[0], x_range[1]), (y_range[0], y_range[1]), (z_range[0], z_range[1])));
    }

    let mut xmin = 0;
    let mut xmax = 0;
    let mut ymin = 0;
    let mut ymax = 0;
    let mut zmin = 0;
    let mut zmax = 0;

    for (command, xrange, yrange, zrange) in commands {
        xmin = min(xrange.0, xmin);
        xmax = max(xrange.1, xmax);
        ymin = min(yrange.0, ymin);
        ymax = max(yrange.1, ymax);
        zmin = min(zrange.0, zmin);
        zmax = max(zrange.1, zmax);
    }

    let lenx = xmax - xmin;
    let leny = ymax - ymin;
    let lenz = zmax - zmin;

    let xstep = lenx / 1000;
    let ystep = leny / 100;
    let zstep = lenz / 100;

    let xfinal = lenx - xstep * 1000;
    let yfinal = leny - ystep * 100;
    let zfinal = lenz - zstep * 100;

    let set = |block: &mut [bool], x: usize, y: usize, z: usize, value: bool| {
        block[x + ystep as usize * y + xstep as usize * ystep as usize * z] = value;
    };

    let get = |block: &mut [bool], x: usize, y: usize, z: usize, value: bool| {
        block[x + ystep as usize * y + xstep as usize * ystep as usize * z]
    };

    let mut block : Vec<bool> = vec![false; xstep as usize * ystep as usize* zstep as usize];

    println!("{}", block.len());

    for start_x in 0..1000 {
        for start_y in 0..100 {
            for start_z in 0..100 {
                // Bruh
                for value in block.iter_mut() {
                    *value = false;
                }
            }
        }
    }

}
