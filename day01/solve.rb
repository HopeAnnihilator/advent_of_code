# part 1
p File.readlines('day01/input').chunk_while{|x, y| x.to_i > y.to_i}.to_a.length - 1
# part 2
p File.readlines('day01/input').map{|x| x.to_i}.each_cons(3).chunk_while{|x, y| x.reduce(:+) >= y.reduce(:+)}.to_a.length - 1