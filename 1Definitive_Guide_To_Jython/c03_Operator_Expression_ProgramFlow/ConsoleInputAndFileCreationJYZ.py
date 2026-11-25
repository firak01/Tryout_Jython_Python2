'''
Created on 31.10.2026

Aus dem Buch "Definitive Guide to Jython", Kapitel 3

@author: Fritz Lindhauer
'''

import os

# Create empty dictionary
player_dict = {}
# Create an empty string
enter_player = ''

# Enter a loop to enter information from keyboard
while enter_player.upper() != 'X':

    print 'Sports Team Administration App'

    # If the file exists, then allow us to manage it, otherwise force creation.
    if os.path.isfile('players.txt'):
        enter_player = raw_input("Would you like to create a team or manage an existing team?\n (Enter 'C' for create, 'M' for manage, 'X' to exit) ")
    else:
        # Force creation of file if it does not yet exist.
        enter_player = 'C'

    # Check to determine which action to take.  C = create, M = manage, X = Exit and Save
    if enter_player.upper() == 'C':

    # Enter a player for the team
        print 'Enter a list of players on our team along with their position'
        enter_cont = 'Y'

        #  While continuing to enter new player's, perform the following
        while enter_cont.upper() == 'Y':
            # Capture keyboard entry into name variable
            name = raw_input('Enter players first name: ')
            # Capture keyboard entry into position variable
            position = raw_input('Enter players position: ')
            # Assign position to a dictionary key of the player name
            player_dict[name] = position
            enter_cont = raw_input("Enter another player? (Press 'N' to exit or 'Y' to continue)")
        else:
            enter_player = 'X'

    # Manage player.txt entries
    elif enter_player.upper() == 'M':

        # Read values from the external file into a dictionary object
        print
        print 'Manage the Team'
        # Open file and assign to playerfile
        playerfile = open('players.txt','r')
        # Use the for-loop to iterate over the entries in the file
        for player in playerfile:
            # Split entries into key/value pairs and add to list
            playerList = player.split(':')
            # Build dictionary using list values from file
            player_dict[playerList[0]] = playerList[1]
        # Close the file
        playerfile.close()

        print 'Team Listing'
        print '++++++++++++'

        # Iterate over dictionary values and print key/value pairs
        for i, player in enumerate(player_dict):
            print 'Player %s Name: %s -- Position: %s' %(i, player, player_dict[player])

else:
    # Save the external file and close resources
    if player_dict:

        print 'Saving Team Data...'
        # Open the file
        playerfile = open('players.txt','w')
        # Write each dictionary element to the file
        for player in player_dict:
            playerfile.write('%s:%s\n' % (player.strip(),player_dict[player].strip()))
        # Close file
        playerfile.close()