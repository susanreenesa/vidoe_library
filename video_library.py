class Customer(object):
    def __init__(self, name,customer_movie_library=[]):
        self.name = name
        self.customer_movie_library = customer_movie_library

class Movie(object):
    def __init__(self,name,category):
        self.name =name
    def price(self):
        if category == [0]:
            return  300*number_of_days_movie_is_retained
        if category == [1]:
            return 500*number_of_days_movie_is_retained
        if category == [2]:
            return  1000*number_of_days_movie_is_retained
class Library(object):
    def __init__(self, movies_available=[], movies_lent=[]):
        self.movies_available = movies_available
        self.movies_lent = movies_lent


if __name__ == "__main__":
    customer = Customer("Ritah")
    library = Library()
    movie_names = []
    category =['children','regular','new_release']
    print "Welcome to Susan\'s library"
    while True:
        choice = int(raw_input("1:Register movies\n2:Lend movies\n3:Return movies\n4:Exit\nEnter a number to do the action (1-4)\n"))

        if choice ==1:
            librarian_name = raw_input("Enter admins name:  ")
            if librarian_name == 'susan':
                while True:
                    #variable to register movies
                        #want to be able to enter many movies at a time
                    name =raw_input('Enter the movies name:   ')
                    category = raw_input('Enter the movie\'s category:  ')
                    movie = Movie(name, category)
                    while True:
                        if category == 'children':
                            break
                        elif category=='regular':
                            break
                        elif category == 'new_release':
                            break
                        else:
                            print "Invalid Entry try again"
                            category = raw_input('Enter the movie\'s category:  ')
                        library.movies_available.append(movie)
                    register_another_movie =raw_input("Would you like to enter another movie? \"Enter y/n\":  ")
                    if register_another_movie == 'y':
                        choice == 1
                    else:
                        break
                #print "These are the movies available"
                movie_names = [(movie.name)for movie in library.movies_available]
                #movie_names =[library.movies_available.append(movie.name)]
                print ( movie_names)
            else:
                print "permission denied!"




        elif choice == 2:
        #registering a customer
            print "Lending out movies"
            customer_name = raw_input('Enter customer\'s name:  ')
            while True:
                movie_name = raw_input('Enter the movie name:  ')
                for x in movie_names:
                    if movie_name == movie_names:
                        library.movies_available.remove(x)
                        customer.customer_movie_library.append(x)
                        library.movies_lent.append(x)
                        print [(b.name for b in library)]
                        #enter number of days the movie will be borrowed
                        number_of_days_to_retain_movie =int(raw_input("Enter number of days the movie is retain"))
                        movie.price()
                    else:
                        print "Movie entered is not available \n"
                lending_more_movies= raw_input("Do you want to lend more movies ? \"Enter y/n\":  ")
                if lending_more_movies =='y':
                    choice =2
                else:
                    break



        elif choice == 3:
        # returning movies
            name_of_movie_returned = raw_input('Enter name of movie returned:  ')
            number_of_days_with_movie = int(raw_input("Enter the number of days spent with the movie: "))
            days_difference = number_of_days_to_retain_movie-number_of_days_with_movie
            for t in customer.customer_movie_library:
                if category ==[2]:
                    if days_difference >= 0:
                        discount = total_price*0.1
                if t.name == name_of_movie_returned:
                    library.movies_available.append(t)
                    customer.customer_movie_library.remove(t)
                    library.movies_lent.remove(t)
        elif choice == 4:
            break
        else:
            print "Invalid selection, try again"



