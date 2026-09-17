"""
==============================================================================
  ROCK, PAPER, SCISSORS   versus   A LEARNING MACHINE
  A small artificial brain that is built from nothing but ADDITION.
==============================================================================

WHAT YOU ARE LOOKING AT
.......................

You are about to play rock, paper, scissors against a computer opponent.
The opponent is an "artificial neural network": a very small artificial
brain. It watches the last five moves you made, tries to guess what you
will play next, and then plays whatever beats that guess.

Every single round it also LEARNS. After you reveal your move, the brain
compares its guess with the truth and nudges its own internal numbers a
little bit into the direction that would have been correct.

THE POINT OF THIS FILE
......................

A computer processor can, deep down, do astonishingly little. It can

    (1) ADD two numbers,
    (2) REPEAT something (a loop),
    (3) COMPARE two numbers and decide what to do next (a condition).

Everything else that a computer ever does is built on top of those three
abilities. To make that visible, this program uses NO other arithmetic.
Search the instructions in this file: there is not one multiplication sign,
not one division sign and not one subtraction sign in the entire program.
The plus sign is the only arithmetic sign that appears.

A minus character shows up in exactly two harmless places:

    (a) in the NUMBER  -1 , which is a number and not an operation,
        in the same way that -1 is a number when you write it on paper, and
    (b) as a printed TEXT character, so that a negative result on screen
        looks like  -1.75  and not like  1.75 .

Everything else, including multiplication, division, subtraction, the whole
neural network and its learning procedure, is written with the plus sign.

HOW TO READ THIS FILE
.....................

The file is divided into parts. Read them in order:

    PART 1   The toolbox: arithmetic made from additions
    PART 2   Numbers with decimal places, made from whole numbers
    PART 3   The rules of rock, paper, scissors
    PART 4   The brain: what it is made of
    PART 5   Thinking: how the brain turns five past moves into a guess
    PART 6   Learning: how the brain corrects itself afterwards
    PART 7   Showing the numbers on screen
    PART 8   The game itself

HOW TO RUN IT
.............

    python3 rock_paper_scissors.py
"""


# ============================================================================
#  PART 1   THE TOOLBOX: ARITHMETIC MADE FROM ADDITIONS
# ============================================================================
#
#  Below we build multiplication and division out of addition. Once these
#  few small helpers exist, the rest of the program can pretend that a
#  computer knows how to multiply. It does not. It only ever adds.
# ============================================================================


# The first of the two harmless minus characters in this file.
# It is not a calculation. It is simply the NUMBER that sits one step to the
# left of zero on the number line. We give it a name so that we can write
# "add MINUS_ONE" instead of "subtract one".
MINUS_ONE = -1

# The second one. It is a piece of TEXT that we print in front of negative
# numbers so that a human reader can recognise them. It is never used to
# calculate anything.
MINUS_SIGN_TEXT = "-"


def flip_sign(value):
    """
    Turn a number into its mirror image on the other side of zero.

        flip_sign(7)   gives  -7
        flip_sign(-7)  gives   7
        flip_sign(0)   gives   0

    HOW IT WORKS
        Imagine two walkers starting at zero. One walks towards the number
        we were given, the other walks the same number of steps in the
        opposite direction. When the first walker arrives, the second one
        is standing exactly on the mirror image.

    WHY WE NEED IT
        This single helper is what replaces subtraction in the entire
        program. "a minus b" is written as "a + flip_sign(b)".
    """
    mirror_image = 0

    if value > 0:
        # The number is to the right of zero, so we walk to the left.
        walker = value
        while walker > 0:
            walker = walker + MINUS_ONE               # one step towards zero
            mirror_image = mirror_image + MINUS_ONE   # one step to the left
    else:
        # The number is at zero or to the left of it, so we walk to the right.
        walker = value
        while walker < 0:
            walker = walker + 1
            mirror_image = mirror_image + 1

    return mirror_image


def absolute_value(value):
    """
    Forget the sign of a number and keep only its size.

        absolute_value(7)   gives  7
        absolute_value(-7)  gives  7

    This is a pure decision: look at the number, and if it is on the wrong
    side of zero, mirror it.
    """
    if value < 0:
        return flip_sign(value)
    return value


def multiply(value, times):
    """
    Multiplication, spelled out as what it really is: repeated addition.

        multiply(5, 3)  means  0 + 5 + 5 + 5  which is  15

    Both numbers are allowed to be negative:

        multiply(5, -3)   means we add -5 three times, giving -15
        multiply(-5, -3)  means we add  5 three times, giving  15

    HOW IT WORKS
        A loop cannot run "-3 times", so we first look at how big the
        counting number is, ignoring its sign. Then we decide, using the
        sign of that counting number, whether we should add the value
        itself or its mirror image. Finally we simply add that step over
        and over again.
    """
    # How many additions do we have to perform?
    number_of_additions = absolute_value(times)

    # What exactly do we add in each single step?
    # If we are asked to add something a negative number of times, the
    # result points the other way, so we add the mirror image instead.
    if times < 0:
        step = flip_sign(value)
    else:
        step = value

    # And now the whole of multiplication: add the step, again and again.
    result = 0
    counter = 0
    while counter < number_of_additions:
        result = result + step
        counter = counter + 1

    return result


def divide(dividend, divisor):
    """
    Division, spelled out as what it really is: repeated addition.

        divide(17, 5)  gives 3, because 5 fits into 17 three times
                       (the leftover 2 is thrown away)

    We ask: "how many times can I take a step of the size of the divisor
    before I arrive at zero?" Taking a step towards zero from a positive
    number means adding the MIRROR IMAGE of the divisor. That is a plus.

    The divisor is always a positive number in this program, which keeps
    this helper short. The dividend may be negative.

    Note that the leftover is dropped, so this always rounds towards zero:
    divide(7, 2) is 3, and divide(-7, 2) is -3.
    """
    quotient = 0

    if dividend >= 0:
        # We stand to the right of zero and step to the left.
        step_towards_zero = flip_sign(divisor)
        remaining = dividend
        while remaining >= divisor:
            remaining = remaining + step_towards_zero
            quotient = quotient + 1
    else:
        # We stand to the left of zero and step to the right.
        remaining = dividend
        while remaining + divisor <= 0:
            remaining = remaining + divisor
            quotient = quotient + MINUS_ONE

    return quotient


def remainder(dividend, divisor):
    """
    What is left over after dividing. Both numbers must be positive here.

        remainder(17, 5)  gives 2, because 5 fits into 17 three times
                          and 2 are left over

    We use this to wrap numbers around in a circle, for example to say
    "the move after scissors is rock again".
    """
    step_towards_zero = flip_sign(divisor)
    remaining = dividend
    while remaining >= divisor:
        remaining = remaining + step_towards_zero
    return remaining


# ============================================================================
#  PART 2   NUMBERS WITH DECIMAL PLACES, MADE FROM WHOLE NUMBERS
# ============================================================================
#
#  A brain needs numbers such as 0.25 or 1.75. A processor is much happier
#  with whole numbers. So we use a very old trick, the same one you use when
#  you count money in cents instead of in euros:
#
#      we agree that the whole number 100 shall MEAN one, 1.00
#      then 250 means 2.50, 25 means 0.25, and -175 means -1.75
#
#  Adding such numbers works without any change: 25 + 25 is 50, and indeed
#  0.25 plus 0.25 is 0.50. Multiplying needs one extra thought, see below.
# ============================================================================


# The whole number that stands for the value one.
ONE = 100


def multiply_decimals(first, second):
    """
    Multiply two numbers that are written in our "100 means one" style.

    WHY THIS NEEDS AN EXTRA STEP
        Take 0.5 times 0.5, which should be 0.25.
        In our style that is 50 times 50, which gives 2500.
        But 2500 would mean 25.00, and that is a hundred times too much.

        The reason is that BOTH numbers were made a hundred times bigger
        before we started, so the result came out ten thousand times too
        big instead of a hundred times too big. We repair it by dividing
        the result once by one hundred, and division is repeated addition.

        2500 divided by 100 is 25, and 25 means 0.25. Correct.
    """
    oversized_result = multiply(first, second)
    return divide(oversized_result, ONE)


# ============================================================================
#  PART 3   THE RULES OF ROCK, PAPER, SCISSORS
# ============================================================================
#
#  Inside the computer there is no such thing as "paper". There are only
#  numbers. So we agree on a translation table:
#
#      0 means rock
#      1 means paper
#      2 means scissors
#
#  The three moves form a circle: rock loses to paper, paper loses to
#  scissors, scissors loses to rock, and then we are back at the start.
#  Walking one step forward in that circle means "the move that wins
#  against this one". Walking off the end brings us back to zero, which is
#  exactly what the leftover helper from PART 1 does for us.
# ============================================================================


MOVE_NAMES = ["rock", "paper", "scissors"]
NUMBER_OF_MOVES = 3


def move_that_beats(move):
    """Give back the move that wins against the move we were given."""
    return remainder(move + 1, NUMBER_OF_MOVES)


def move_that_loses_to(move):
    """Give back the move that loses against the move we were given."""
    return remainder(move + 2, NUMBER_OF_MOVES)


def judge_round(human_move, computer_move):
    """
    Decide who won a single round.
    Gives back the text "human", "computer" or "draw".
    """
    if human_move == computer_move:
        return "draw"
    if computer_move == move_that_loses_to(human_move):
        return "human"
    return "computer"


# ============================================================================
#  PART 4   THE BRAIN: WHAT IT IS MADE OF
# ============================================================================
#
#  The brain is a so called neural network. Do not let the name frighten
#  you. It is a bag of numbers plus a rule for adding them up.
#
#  It is organised in three layers:
#
#      INPUT LAYER     15 neurons, describing your last five moves
#           |
#           |  every input is connected to every hidden neuron:
#           |  15 times 6 makes 90 connections, each with its own weight
#           |
#      HIDDEN LAYER     6 neurons, the "thinking" middle layer
#           |
#           |  every hidden neuron is connected to every output:
#           |  6 times 3 makes 18 further connections
#           |
#      OUTPUT LAYER     3 neurons, one per move, saying how strongly the
#                       brain expects rock, paper and scissors next
#
#  A WEIGHT is just a number attached to a connection. It says how loudly
#  the thing on the left is allowed to shout at the thing on the right.
#  A large positive weight means "when this input is active, switch the
#  neuron on". A negative weight means "when this input is active, keep
#  the neuron quiet". Learning means nothing more than carefully changing
#  those weights.
#
#  WHY 15 INPUT NEURONS FOR FIVE MOVES?
#  A neuron cannot understand the word "paper". And feeding in a single
#  number for each past move would be misleading, because it would suggest
#  that paper is somehow "one more" than rock. Instead we give every past
#  move THREE input neurons, of which exactly one is switched on:
#
#      you played rock      the three become   ONE   0     0
#      you played paper     the three become   0     ONE   0
#      you played scissors  the three become   0     0     ONE
#
#  Five past moves, three neurons each, makes fifteen input neurons. Rounds
#  that have not been played yet simply stay at zero everywhere.
#
#  WHY 3 OUTPUT NEURONS AND NOT 1?
#  We could have used a single output neuron and read its number as "0
#  means rock, 1 means paper, 2 means scissors". That would be a trap.
#  It would quietly claim that paper lies BETWEEN rock and scissors, and
#  that rock and scissors are twice as far apart as rock and paper. In
#  this game that is nonsense: no move is further from any other.
#
#  Giving each move its own neuron avoids the whole problem. The three
#  outputs are simply three separate opinions, with no order and no
#  distance between them at all:
#
#      output 1   how strongly it expects ROCK
#      output 2   how strongly it expects PAPER
#      output 3   how strongly it expects SCISSORS
#
#  This is the same trick we just used for the inputs, and for the same
#  reason. Whichever of the three shouts loudest is the brain's guess.
#
#  It also lets the brain be genuinely undecided in a way a single number
#  never could. Scores of 0.45 for rock, 0.10 for paper and 0.45 for
#  scissors say "either rock or scissors, but certainly not paper". One
#  number could only have answered "1", which means paper: exactly the
#  wrong answer.
# ============================================================================


HISTORY_LENGTH = 5                   # how many past moves the brain sees
NUMBER_OF_INPUTS = 15                # five moves, three input neurons each
NUMBER_OF_HIDDEN = 6                 # neurons in the middle layer
NUMBER_OF_OUTPUTS = 3                # one score per possible next move

# How careful the brain is when it corrects itself. The correction is
# divided by this number before it is applied, so a LARGER number here
# means SMALLER, more cautious steps. Try changing it during the lecture:
# a very large value makes the machine a slow learner, a very small one
# makes it jumpy and superstitious, believing whatever happened last.
LEARNING_CAUTION = 4


# The weights themselves. These lists ARE the brain. Everything the machine
# ever learns about you ends up in these numbers and nowhere else.
weights_input_to_hidden = []     # 15 lists of 6 numbers each
hidden_bias = []                 # 6 numbers
weights_hidden_to_output = []    # 6 lists of 3 numbers each
output_bias = []                 # 3 numbers

# A "bias" is a weight that is not attached to any input. It is simply added
# to a neuron every time, and lets the neuron have an opinion of its own,
# independent of what it is being told.


# ............................................................................
#  Random numbers, also made from additions
# ............................................................................
#
#  The brain must not start with all weights equal, otherwise all six
#  hidden neurons would think exactly the same thought forever. So we need
#  some randomness. A computer has none. It fakes it with a recipe that
#  produces numbers which merely LOOK unpredictable:
#
#      take the previous number, multiply it, add something,
#      and keep only the leftover after dividing by a fixed number
#
#  Multiplication is repeated addition, and the leftover comes from repeated
#  addition too, so this is once again nothing but plus signs.
# ............................................................................

random_seed = 1234


def next_random_number():
    """Give back the next number in our pretend random sequence."""
    global random_seed
    stirred = multiply(random_seed, 75) + 74
    random_seed = remainder(stirred, 65537)
    return random_seed


def random_small_weight():
    """
    Give back a small starting weight, somewhere between -0.25 and 0.25,
    which in our "100 means one" style is between -25 and 25.
    """
    inside_zero_to_fifty = remainder(next_random_number(), 51)
    return inside_zero_to_fifty + flip_sign(25)


def build_brain():
    """Create the brain and fill every weight with a small random number."""
    for input_index in range(NUMBER_OF_INPUTS):
        row = []
        for hidden_index in range(NUMBER_OF_HIDDEN):
            row.append(random_small_weight())
        weights_input_to_hidden.append(row)

    for hidden_index in range(NUMBER_OF_HIDDEN):
        hidden_bias.append(0)

    for hidden_index in range(NUMBER_OF_HIDDEN):
        row = []
        for output_index in range(NUMBER_OF_OUTPUTS):
            row.append(random_small_weight())
        weights_hidden_to_output.append(row)

    for output_index in range(NUMBER_OF_OUTPUTS):
        output_bias.append(0)


def build_inputs_from_history(history):
    """
    Switch on the right input neurons for the moves you have played so far.
    The most recent move uses the first three input neurons, the move before
    that the next three, and so on, five moves back in time.
    """
    inputs = []
    for neuron in range(NUMBER_OF_INPUTS):
        inputs.append(0)

    # We walk backwards through your history, starting at the newest move.
    how_far_back = 0
    position_in_history = len(history) + MINUS_ONE

    while how_far_back < HISTORY_LENGTH:
        if position_in_history >= 0:
            move = history[position_in_history]
            # Each step back in time skips three input neurons.
            first_neuron_of_this_move = multiply(how_far_back, 3)
            inputs[first_neuron_of_this_move + move] = ONE
        how_far_back = how_far_back + 1
        position_in_history = position_in_history + MINUS_ONE

    return inputs


# ============================================================================
#  PART 5   THINKING: HOW THE BRAIN TURNS FIVE PAST MOVES INTO A GUESS
# ============================================================================
#
#  This is called FORWARD PROPAGATION, because information travels forward
#  through the layers: inputs, then hidden neurons, then the output.
#
#  A single neuron does exactly two things:
#
#      STEP A   It adds up everything it is told, where every incoming
#               number is first weighted, that is multiplied by the weight
#               of its connection. Plus its own bias.
#
#      STEP B   It decides whether to pass the result on. Our hidden
#               neurons use the simplest possible decision in the world:
#
#                   if the sum is above zero, pass it on unchanged
#                   otherwise, stay silent and pass on zero
#
#               That rule has a fancy name, "rectified linear unit", but as
#               you can see it is a single comparison. No exotic mathematics
#               is hiding anywhere.
#
#  That is all. Repeat it for six hidden neurons and one output neuron and
#  you have a thinking machine.
# ============================================================================


def think(inputs):
    """
    Run the inputs through the brain and give back three things:

        hidden_sums     what each hidden neuron added up (before deciding)
        hidden_values   what each hidden neuron actually passed on
        output_values   the three numbers the output neurons produced

    We hand back the intermediate results as well, because the learning
    procedure in PART 6 needs to know what happened on the way.
    """

    # ........................................................
    #  LAYER ONE: from the 15 input neurons to the 6 hidden ones
    # ........................................................
    hidden_sums = []
    hidden_values = []

    for hidden_index in range(NUMBER_OF_HIDDEN):

        # STEP A: add up all the weighted inputs, starting from the bias.
        running_total = hidden_bias[hidden_index]

        for input_index in range(NUMBER_OF_INPUTS):
            input_value = inputs[input_index]

            # Most input neurons are switched off, and a weighted zero is
            # still zero. Adding zero changes nothing, so we may skip it.
            # This is a shortcut for speed only, never for the result.
            if input_value != 0:
                weight = weights_input_to_hidden[input_index][hidden_index]
                contribution = multiply_decimals(input_value, weight)
                running_total = running_total + contribution

        hidden_sums.append(running_total)

        # STEP B: the decision. Silent below zero, honest above it.
        if running_total > 0:
            passed_on = running_total
        else:
            passed_on = 0

        hidden_values.append(passed_on)

    # ........................................................
    #  LAYER TWO: from the 6 hidden neurons to the 3 output neurons
    # ........................................................
    output_values = []

    for output_index in range(NUMBER_OF_OUTPUTS):

        running_total = output_bias[output_index]

        for hidden_index in range(NUMBER_OF_HIDDEN):
            weight = weights_hidden_to_output[hidden_index][output_index]
            contribution = multiply_decimals(hidden_values[hidden_index],
                                             weight)
            running_total = running_total + contribution

        output_values.append(running_total)

    # The output neurons pass their sums on as they are. They make no yes
    # or no decision, because we are not asking "yes or no", we are asking
    # "how strongly do you expect this move?".

    return hidden_sums, hidden_values, output_values


def loudest_output(output_values):
    """
    Which of the three output neurons is shouting loudest? That one is the
    brain's guess.

    This is pure comparing: walk along the three numbers, remember the best
    one seen so far, and replace it whenever a louder one turns up.
    """
    loudest_move = 0
    loudest_score = output_values[0]

    position = 1
    while position < NUMBER_OF_OUTPUTS:
        if output_values[position] > loudest_score:
            loudest_score = output_values[position]
            loudest_move = position
        position = position + 1

    return loudest_move


# ============================================================================
#  PART 6   LEARNING: HOW THE BRAIN CORRECTS ITSELF AFTERWARDS
# ============================================================================
#
#  This is called BACKWARD PROPAGATION, or backpropagation, because now the
#  information travels the other way: from the mistake at the output back
#  through the layers to the weights that caused it.
#
#  The idea is embarrassingly simple, and it is the same idea a person uses
#  when adjusting the tap in a shower:
#
#      1  Say what SHOULD have happened.
#      2  Compare it with what DID happen. The difference is the mistake.
#      3  Ask every weight: "how much of this mistake is your fault?"
#         A connection is guilty in proportion to how loudly it shouted.
#      4  Nudge every weight a little bit against its own guilt.
#         Little, because one round is only one piece of evidence.
#
#  Step 3 is the only step that looks mysterious, and it is not. If a hidden
#  neuron was completely silent, it cannot possibly have caused the mistake,
#  so its weights stay untouched. If it shouted loudly, it gets most of the
#  blame. The blame is therefore "mistake, weighted by how loud you were",
#  which is once again a multiplication, which is once again repeated adding.
# ============================================================================


def learn(inputs, hidden_sums, hidden_values, output_values, actual_move):
    """
    Improve the brain, now that we know which move the human really played.
    """

    # ........................................................
    #  STEP 1: what SHOULD the three outputs have been?
    # ........................................................
    #  The perfect answer is full confidence on the move that was really
    #  played, and nothing at all on the other two.
    wanted_values = []
    for output_index in range(NUMBER_OF_OUTPUTS):
        if output_index == actual_move:
            wanted_values.append(ONE)
        else:
            wanted_values.append(0)

    # ........................................................
    #  STEP 2: the mistake at each output
    # ........................................................
    #  "how much too loud was I?" is the score minus the wanted score,
    #  which we write as the score PLUS the mirror image of the wanted one.
    #  A positive mistake means the brain was too confident about that move,
    #  a negative one means it was not confident enough.
    output_mistakes = []
    for output_index in range(NUMBER_OF_OUTPUTS):
        mistake = (output_values[output_index]
                   + flip_sign(wanted_values[output_index]))
        output_mistakes.append(mistake)

    # ........................................................
    #  STEP 3: pass the blame back to the hidden neurons
    # ........................................................
    #  A hidden neuron is to blame for each of the three mistakes in
    #  proportion to the weight of its connection to that output, so it
    #  collects three pieces of blame and adds them up. We collect all the
    #  blame BEFORE changing any weight, because we want to hand out the
    #  blame using the same brain that made the mistake.
    hidden_mistakes = []

    for hidden_index in range(NUMBER_OF_HIDDEN):
        collected_blame = 0

        for output_index in range(NUMBER_OF_OUTPUTS):
            weight = weights_hidden_to_output[hidden_index][output_index]
            share_of_blame = multiply_decimals(output_mistakes[output_index],
                                               weight)
            collected_blame = collected_blame + share_of_blame

        # A neuron that stayed silent had no influence at all, so it carries
        # no blame. This is the mirror image of the decision made in PART 5.
        if hidden_sums[hidden_index] > 0:
            hidden_mistakes.append(collected_blame)
        else:
            hidden_mistakes.append(0)

    # ........................................................
    #  STEP 4: nudge the eighteen weights that lead into the outputs
    # ........................................................
    for hidden_index in range(NUMBER_OF_HIDDEN):
        for output_index in range(NUMBER_OF_OUTPUTS):

            # How guilty is this one connection? The mistake at that output,
            # weighted by how loudly this hidden neuron was speaking.
            guilt = multiply_decimals(output_mistakes[output_index],
                                      hidden_values[hidden_index])

            # Take only a small fraction of the guilt, so that one single
            # round cannot overturn everything learned before.
            correction = divide(guilt, LEARNING_CAUTION)

            # Move AGAINST the guilt, therefore the mirror image.
            old_weight = weights_hidden_to_output[hidden_index][output_index]
            weights_hidden_to_output[hidden_index][output_index] = (
                old_weight + flip_sign(correction))

    #  A bias is treated exactly like a weight whose input is always one.
    for output_index in range(NUMBER_OF_OUTPUTS):
        correction = divide(output_mistakes[output_index], LEARNING_CAUTION)
        output_bias[output_index] = (output_bias[output_index]
                                     + flip_sign(correction))

    # ........................................................
    #  STEP 5: nudge the ninety weights between inputs and hidden layer
    # ........................................................
    #  Exactly the same procedure, one layer further back.
    for input_index in range(NUMBER_OF_INPUTS):
        input_value = inputs[input_index]

        # An input neuron that was switched off had no influence, so its
        # weights stay exactly as they are.
        if input_value != 0:
            for hidden_index in range(NUMBER_OF_HIDDEN):

                guilt = multiply_decimals(hidden_mistakes[hidden_index],
                                          input_value)
                correction = divide(guilt, LEARNING_CAUTION)

                old_weight = weights_input_to_hidden[input_index][hidden_index]
                weights_input_to_hidden[input_index][hidden_index] = (
                    old_weight + flip_sign(correction))

    for hidden_index in range(NUMBER_OF_HIDDEN):
        correction = divide(hidden_mistakes[hidden_index], LEARNING_CAUTION)
        hidden_bias[hidden_index] = hidden_bias[hidden_index] + flip_sign(correction)


# ============================================================================
#  PART 7   SHOWING THE NUMBERS ON SCREEN
# ============================================================================


def format_decimal(value):
    """
    Turn one of our "100 means one" whole numbers into readable text.

        250 becomes "2.50",  25 becomes "0.25",  -175 becomes "-1.75"

    We split the number into the part before the dot and the part after it.
    The part before the dot is the number of whole hundreds, which is a
    division. The part after the dot is what is left over.
    """
    size = absolute_value(value)
    whole_part = divide(size, ONE)
    fraction_part = remainder(size, ONE)

    fraction_text = str(fraction_part)
    if fraction_part < 10:
        fraction_text = "0" + fraction_text

    text = str(whole_part) + "." + fraction_text
    if value < 0:
        text = MINUS_SIGN_TEXT + text
    return text


def bar_of_blocks(count):
    """
    Draw one bar of the score chart: a row of blocks, added one at a time.

    This is what a bar chart really is. There is no drawing going on, only
    a piece of text that grows by one block at a time until it is as long
    as the number it stands for.
    """
    bar = ""
    drawn = 0
    while drawn < count:
        bar = bar + "#"
        drawn = drawn + 1
    return bar


def show_scoreboard(human_wins, computer_wins, draws):
    """Show the score as three bars, one block per round won."""
    print("    you       " + bar_of_blocks(human_wins).ljust(20)
          + " " + str(human_wins))
    print("    machine   " + bar_of_blocks(computer_wins).ljust(20)
          + " " + str(computer_wins))
    print("    draws     " + bar_of_blocks(draws).ljust(20)
          + " " + str(draws))


def show_history(history):
    """Print the moves the brain can see, newest on the right."""
    if len(history) == 0:
        return

    start = 0
    if len(history) > HISTORY_LENGTH:
        start = len(history) + flip_sign(HISTORY_LENGTH)

    shown = []
    position = start
    while position < len(history):
        shown.append(MOVE_NAMES[history[position]])
        position = position + 1

    print("  the five moves the brain can see: " + ", ".join(shown))


# ============================================================================
#  PART 8   THE GAME ITSELF
# ============================================================================


def read_human_move():
    """
    Ask the human for a move. Gives back a move number, or the text "quit",
    or the text "again" if the input made no sense.
    """
    answer = input("  your move (rock, paper, scissors)  >  ").strip().lower()

    if answer in ["r", "rock"]:
        return 0
    if answer in ["p", "paper"]:
        return 1
    if answer in ["s", "scissors"]:
        return 2
    if answer in ["q", "quit"]:
        return "quit"

    print("  please type  rock ,  paper ,  scissors  or  quit")
    return "again"


def play():
    """The main game loop: one turn of the loop is one round of the game."""

    build_brain()

    history = []          # every move the human has played, oldest first
    human_wins = 0
    computer_wins = 0
    draws = 0
    round_number = 0

    print("")
    print("  ROCK, PAPER, SCISSORS against a machine that learns.")
    print("  Every calculation inside this program is an addition.")
    print("  Type  rock ,  paper ,  scissors  or  quit .")

    while True:
        round_number = round_number + 1
        print("")
        print("  ROUND " + str(round_number))
        show_history(history)

        # The machine thinks FIRST, before it can see your new move.
        inputs = build_inputs_from_history(history)
        hidden_sums, hidden_values, output_values = think(inputs)

        predicted_move = loudest_output(output_values)
        computer_move = move_that_beats(predicted_move)

        print("  its three output neurons say:  rock "
              + format_decimal(output_values[0])
              + "   paper " + format_decimal(output_values[1])
              + "   scissors " + format_decimal(output_values[2]))
        print("  so it expects " + MOVE_NAMES[predicted_move].upper()
              + " and plays " + MOVE_NAMES[computer_move].upper())

        # Now the human plays.
        human_move = read_human_move()
        while human_move == "again":
            human_move = read_human_move()

        if human_move == "quit":
            round_number = round_number + MINUS_ONE
            break

        # Who won?
        print("  you played " + MOVE_NAMES[human_move].upper()
              + ", the machine had " + MOVE_NAMES[computer_move].upper())

        winner = judge_round(human_move, computer_move)
        if winner == "human":
            human_wins = human_wins + 1
            print("  YOU WIN this round.")
        elif winner == "computer":
            computer_wins = computer_wins + 1
            print("  THE MACHINE WINS this round.")
        else:
            draws = draws + 1
            print("  a DRAW.")

        show_scoreboard(human_wins, computer_wins, draws)

        # And now the machine learns from what just happened.
        learn(inputs, hidden_sums, hidden_values, output_values, human_move)

        history.append(human_move)

    print("")
    print("  after " + str(round_number) + " rounds:")
    show_scoreboard(human_wins, computer_wins, draws)
    print("  every one of those decisions came from additions alone.")
    print("")


if __name__ == "__main__":
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print("")
        print("  goodbye.")
