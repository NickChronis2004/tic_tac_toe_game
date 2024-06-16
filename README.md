ΟΝΟΜΑ:ΝΙΚΟΛΑΟΣ ΧΡΟΝΗΣ 
NAME: NIKOLAOS CHRONIS

DATE: 06/2024

(greek version)
Ακολουθει μια αναλυση του project μου καθως και οδηγιες για το πως να το εκτελεσετε:

main.py: Αυτό το script δημιουργεί ένα απλό γραφικό περιβάλλον (δυο κουμπια) χρησιμοποιώντας τη βιβλιοθήκη tkinter, το οποίο επιτρέπει στον χρήστη να επιλέξει μεταξύ δυο modes ενος παιχνιδιου tic tac toe, με εναν ή δυο παικτες αντιστοιχα.


singleplayer_mode.py: Αυτό το script δημιουργεί ένα παιχνίδι Tic Tac Toe με γραφικό περιβάλλον.Το παιχνίδι έχει επιλογές με διαφορετικά επίπεδα δυσκολίας για τον υπολογιστή. Ακολουθεί μια αναλυτική εξήγηση των λειτουργιών και της δομής του κώδικα:

    Λειτουργίες για αλλαγή δυσκολίας: changeDifficultyEasy, changeDifficultyMid, changeDifficultyHard για την αλλαγή της δυσκολίας του παιχνιδιού και την ενημέρωση της εμφάνισης των κουμπιών.
    
    updateBoard: Ενημερώνει το γραφικό περιβάλλον με την τρέχουσα κατάσταση του ταμπλό.
    
    checkForWin: Ελέγχει αν υπάρχει νικητής και επιστρέφει τη νικητήρια συνδυαστική γραμμή.
    
    mark_position: Στρατηγική του υπολογιστή για τοποθέτηση συμβόλου στο ταμπλό.
    
    checkForDraw: Ελέγχει αν το παιχνίδι έχει λήξει με ισοπαλία.
    
    restartGame: Επανεκκινεί το παιχνίδι.
    
    minimax: Αλγόριθμος Minimax για τη στρατηγική του υπολογιστή στο επίπεδο δυσκολίας "hard".
    
    Επίπεδα δυσκολίας για τον υπολογιστή: level_easy, level_mid, level_hard για τα επίπεδα εύκολο, μεσαίο και δύσκολο αντίστοιχα.
    
    playComputer: Διαχείριση της κίνησης του υπολογιστή.
    
    highlightWinner: Επισημαίνει τις θέσεις που αποτελούν νικητήρια συνδυαστική γραμμή.
    
    play: Διαχειρίζεται την κίνηση του παίκτη όταν πατάει ένα κουμπί στο ταμπλό.
    
    hint: Παρέχει υπόδειξη για την καλύτερη κίνηση που μπορεί να κάνει ο παίκτης.
    
    Γραφικό Περιβάλλον (UI):
        
        Κουμπιά για επιλογή δυσκολίας: easyButton, midButton, hardButton.
        
        Κουμπί "Hint": hintButton.    
        
        Κουμπιά ταμπλό: 9 κουμπιά για τις θέσεις του ταμπλό.
        
        Κουμπί "Restart Game": restartButton για την επανεκκίνηση του παιχνιδιού.

server.py: Υλοποιεί έναν απλό server για ένα παιχνίδι Tic Tac Toe που λειτουργεί μεταξύ δύο παικτών.Πιο συγκεκριμενα: 

    handle_client: Αυτή η συνάρτηση διαχειρίζεται την επικοινωνία με έναν πελάτη που συνδέεται στον server.
    
    client_socket: Το socket για την επικοινωνία με τον πελάτη.
    
    addr: Η διεύθυνση του πελάτη.
    
    other_client: Το socket του άλλου πελάτη που συμμετέχει στο παιχνίδι.
    
    turn: Μια λίστα με ένα στοιχείο (π.χ. ['X']) για τη σειρά του παίκτη.
    
    wins: Ένα λεξικό για την καταγραφή των νικών κάθε παίκτη.

    main: Αυτή η συνάρτηση εκκινεί τον server και διαχειρίζεται τις συνδέσεις των παικτών.
    Δημιουργεί ένα socket για IPv4 και TCP (socket.socket(socket.AF_INET, socket.SOCK_STREAM)).
    Δεσμεύει τη διεύθυνση ("0.0.0.0", 9999) και αρχίζει να ακούει για συνδέσεις (server.listen(2)).
    Αποδέχεται τις συνδέσεις από δύο παίκτες (client1 και client2).
    Αποστέλλει καλωσορίσματα στους παίκτες με τις αρχικές σειρές ("Welcome Player 1:X" και "Welcome Player 2:O").
    Ξεκινά δύο ξεχωριστά νήματα για την επικοινωνία με κάθε παίκτη, χρησιμοποιώντας τη συνάρτηση handle_client.

client.py: Ο κώδικας client.py αναλαμβάνει να επικοινωνεί με τον server και να διαχειρίζεται την εμφάνιση του γραφικού περιβάλλοντος για ένα παιχνίδι Tic Tac Toe. Ας δούμε σύντομα τι κάνει κάθε συνάρτηση στον κώδικα:

    check_winner: Ελέγχει αν υπάρχει νικητής στο παιχνίδι Tic Tac Toe.

    receive_messages: Αναλαμβάνει να λαμβάνει μηνύματα από τον server και να ενημερώνει το γραφικό περιβάλλον και το state του παιχνιδιού ανάλογα με τα ληφθέντα μηνύματα.

    send_move: Στέλνει ένα μήνυμα στον server με την κίνηση που έγινε (σύμβολο και θέση).

    on_button_click: Καλείται όταν γίνει κλικ σε ένα κουμπί στο γραφικό περιβάλλον και επικοινωνεί την κίνηση στον server, ανάλογα με τη σειρά του παίκτη.

    reset_game: Στέλνει ένα μήνυμα στον server για να επαναφέρει το παιχνίδι σε κατάσταση εκκίνησης.
    
    clear_board: Εκκαθαρίζει το πίνακα του παιχνιδιού στο γραφικό περιβάλλον.

    create_play_button: Δημιουργεί το κουμπί για επανεκκίνηση του παιχνιδιού.

    update_score: Ενημερώνει την ετικέτα που δείχνει τις νίκες των παικτών.

    on_closing: Κλείνει τη σύνδεση με τον server κατά το κλείσιμο του γραφικού περιβάλλοντος.

Οδηγιες εκτελεσης:

Για να τρεξετε το παιχνιδι ,μπορειτε να ξεκινησετε εκτελωντας την main.py και επιλεγοντας το mode που επιθυμειτε. Το singleplayer mode ειναι αρκετα ευκολο στη χρηση και δεν θα αντιμετωπησετε δυσκολιες. Αν επιλεξετε το multiplayer mode τοτε θα ανοιξει ο server αναμενοντας καποιο αιτημα συνδεσης. Θα πρεπει να τρεξετε το client.py μεσω του command prompt ως εξης:
κανετε cpoy το path του φακελου στο οποιο βρισκεται το αρχειο client.py ,ανοιγετε το τερματικο και στη συνεχεια ανοιγετε τον φακελο με την ενοτλη "cd 'paste_your_path_here' ".Τελος εκτελειτε το αρχειο με την εντολη "python client.py". Θα χρειαστειτε δυυο clients συνεπως θα πρεπει να ανοιξετε και μια καινουρια καρτελα command prompt και να κανετε παλι ακριβως την ιδια διαδικασια. Μπορειτε ωστοσο να παιξετε και απο δυο διαφορετικες συσκευες (πχ απο το κινητο σας μεσω της εφαρμογης pydroid) οπου θα πρεπει να τρεξετε απλως το client.py μεσω ενος IDE. 

!!!ΠΑΡΑΤΗΡΗΣΕΙΣ!!!

1)Βεβαιωθειτε οτι ο υπολογιστης σας εχει εγκατεστημενη την python3

2)Βεβαιωθειτε οτι παντα τρεχετε πρωτα τον server και μετα τους clients

3)Η συνδεση με διαφορετικες συσκευες θα λειτουργησει μονο στην περιπτωση οπου ολες ειναι συνδεδεμενες στο ιδιο wifi και λειτουργουν μονο σε τοπικο δικτυο (localhost)

4)Βεβαιωθειτε οτι εχετε αλλαξει την IP με την δικη σας IP στο σημειο:
# Setup the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('enter_your_local_ip', 9999))

Αυτο μπορειτε να το κανετε με το command prompt μεσω της εντολης 'ipconfig' εκει οπου λεει
IPv4 Address.


(english version)
Following is an analysis of my project and instructions on how to execute it:

main.py: This script creates a simple graphical interface (two buttons) using the tkinter library, allowing the user to choose between two modes of a Tic Tac Toe game, with one or two players respectively.

singleplayer_mode.py: This script creates a Tic Tac Toe game with a graphical interface. The game offers different difficulty levels for the computer player. Here's a detailed explanation of the functions and code structure:

Functions for changing difficulty: changeDifficultyEasy, changeDifficultyMid, changeDifficultyHard adjust the game's difficulty and update button appearances.
updateBoard: Updates the graphical interface with the current state of the board.
checkForWin: Checks for a winner and returns the winning combination.
mark_position: Computer's strategy for placing symbols on the board.
checkForDraw: Checks if the game has ended in a draw.
restartGame: Restarts the game.
minimax: Minimax algorithm for the computer's strategy at "hard" difficulty level.
Difficulty levels: level_easy, level_mid, level_hard for easy, medium, and hard difficulty levels respectively.
playComputer: Manages the computer's moves.
highlightWinner: Highlights positions that form a winning combination.
play: Manages player's move when clicking a button on the board.
hint: Provides hints for the player's best possible move.
UI Components:

Buttons for difficulty selection: easyButton, midButton, hardButton.
"Hint" button: hintButton.
Board buttons: 9 buttons representing board positions.
"Restart Game" button: restartButton for game reset.
server.py: Implements a simple server for a two-player Tic Tac Toe game:

handle_client: Manages communication with a client connecting to the server.
client_socket: Socket for communicating with the client.
addr: Client's address.
other_client: Socket of the other client participating in the game.
turn: List with one element (e.g., ['X']) indicating the player's turn.
wins: Dictionary for recording each player's wins.
main: Starts the server and manages player connections.
client.py: This script communicates with the server and manages the graphical interface for a Tic Tac Toe game. Here's a brief overview of each function in the code:

check_winner: Checks if there's a winner in the Tic Tac Toe game.
receive_messages: Receives messages from the server and updates the graphical interface and game state accordingly.
send_move: Sends a message to the server with the move made (symbol and position).
on_button_click: Triggered when a button on the graphical interface is clicked, communicates the move to the server based on the player's turn.
reset_game: Sends a message to the server to reset the game to its initial state.
clear_board: Clears the game board in the graphical interface.
create_play_button: Creates the button for restarting the game.
update_score: Updates the label displaying players' wins.
on_closing: Closes the connection with the server when the graphical interface is closed.
Execution Instructions:

To run the game, start by executing main.py and selecting the desired mode. The singleplayer mode is user-friendly and straightforward to use. If you choose multiplayer mode, the server will start, awaiting connection requests. You should run client.py via the command prompt as follows:

Copy the path of the folder containing client.py.
Open the terminal and navigate to the folder using cd 'paste_your_path_here'.
Finally, execute the script with python client.py.
You will need two clients, so open a new command prompt tab and repeat the above process. Alternatively, you can play from two different devices (e.g., from your mobile using an IDE like Pydroid) by simply running client.py via an IDE.

Notes:

Ensure Python 3 is installed on your computer.
Always start the server before the clients.
Connecting different devices works only if all are connected to the same Wi-Fi and operate within a local network (localhost).
Make sure to replace the IP address in the code with your local IP using ipconfig command where it says


# Setup the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('enter_your_local_ip', 9999))
This can be done via command prompt using ipconfig, where you'll find the IPv4 Address.