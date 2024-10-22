# TODO Найдите количество книг, которое можно разместить на дискете
disc_vol = 1.44 * 1024 * 1024 # Disc volume, bites
num_of_pages = 100 # Number of pages in book
num_of_lines = 50 # Number of lines on page
num_of_symbs = 25 # Number of symbols in line
symb_weight = 4 # Weight of symbol
book_weight = num_of_pages * num_of_lines * num_of_symbs * symb_weight # Book weight, bites
books_on_disc = int(disc_vol // book_weight)
print("Количество книг, помещающихся на дискету:", books_on_disc)
