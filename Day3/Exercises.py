#Password Strength Checker
import re
from collections import Counter

def check_password_strength(password):
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")

    # Check for at least one number
    if not re.search(r'[0-9]', password):
        print("Password must contain at least one number.")

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password must contain at least one special character.")

    # If all conditions are met
    if (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        print("Password is strong.")
    else:
        print("Password is weak. Please meet the above requirements.")
        newpassword = input("Please try again: ")
        check_password_strength(newpassword)

print("######################### Check Password Strength #########################")
pwd = input("Enter your password: ")
check_password_strength(pwd)
print("######################### Word Frequency Counter #########################")
#Word Frequency Counter
def count_words(text):
    # Convert the text to lowercase to ensure case-insensitive matching
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas iaculis lobortis lorem. Curabitur at metus sed metus gravida scelerisque sit amet ac nunc. Donec molestie dignissim ipsum, at ultrices risus tincidunt id. In gravida felis quis mauris porttitor, vel posuere metus molestie. Proin id ante risus. Morbi volutpat et enim non malesuada. Sed tincidunt, metus dapibus vulputate malesuada, elit orci vulputate eros, commodo pulvinar mi ex in risus. Praesent purus nisi, eleifend eget tristique eu, finibus dapibus nibh. Suspendisse malesuada diam a nulla lobortis, non rutrum turpis venenatis. Praesent et tempor sapien, quis posuere massa.
    
    Praesent ac finibus purus. Vestibulum accumsan, dolor vitae efficitur lacinia, odio urna vestibulum augue, id tristique metus nibh et nulla. Nam faucibus ante eget libero consequat molestie. Ut odio sem, tempor nec viverra vitae, rutrum mollis quam. Mauris sed augue nec lorem vehicula sagittis vitae accumsan magna. Aliquam consequat, justo porttitor condimentum scelerisque, ex nibh placerat nibh, et maximus lorem dolor elementum ligula. Quisque quis nibh nunc.
    
    Morbi molestie in sapien eu cursus. Maecenas ut velit a risus bibendum vestibulum eleifend sit amet neque. Sed imperdiet est sed nisl fermentum, sed porta purus ultricies. Duis rhoncus varius magna, vel scelerisque elit. Nunc nec scelerisque risus. Donec lacus sem, scelerisque vitae eleifend eu, lobortis sit amet nisl. Aenean sodales, nibh venenatis elementum efficitur, nisl augue bibendum lorem, ac blandit libero purus non arcu. Cras blandit lectus non imperdiet tristique. Aenean eu neque id dolor iaculis fringilla. Quisque convallis consectetur orci gravida fermentum.
    
    Donec auctor nulla quis nisi scelerisque, vel iaculis ex dictum. Phasellus elementum nisi id orci lobortis, eu aliquam felis viverra. In luctus purus quam, tempus lacinia tortor egestas et. Nam convallis diam turpis, sed vestibulum nulla accumsan ut. Donec vel congue lacus, lobortis eleifend lacus. Aliquam eleifend fermentum dui, at suscipit neque cursus quis. Duis sed bibendum nibh, et eleifend enim. Quisque facilisis urna turpis, ut porttitor erat vehicula quis. Nulla gravida ornare neque, sed scelerisque ligula aliquam pharetra. Nullam nibh dui, ultrices at sollicitudin ut, bibendum id lectus.
    
    Quisque faucibus egestas pretium. Morbi sit amet eleifend diam. Suspendisse quis nisl ligula. Morbi iaculis ipsum a pharetra tincidunt. Sed maximus tempus ipsum, sit amet lobortis dui ullamcorper dapibus. Suspendisse commodo, tortor eu tempus auctor, libero quam vestibulum lectus, sit amet ultricies purus eros pellentesque ex. Praesent ultricies quam ac mi scelerisque ornare. Maecenas elementum vulputate lectus. Duis sit amet sem aliquam, aliquet eros in, pulvinar massa. Sed faucibus sed ipsum rutrum consequat. Ut ac est quis sem euismod sollicitudin. 
    """.lower()

    # Use regular expression to extract words (ignoring punctuation)
    words = re.findall(r'\b\w+\b', text)

    # Use Counter to count occurrences of each word
    word_counts = Counter(words)

    # Get the top 5 most common words
    top_5_words = word_counts.most_common(5)

    # Display the top 5 words
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word}: {count}")

txt = input("Enter a string: ")
count_words(txt)
