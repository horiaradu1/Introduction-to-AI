import java.util.ArrayList;

import static java.lang.Integer.*;

/**
 *
 * @author Mbassip2
 */
public class Othello {

    public static final int SQUARESIZE= 60;   // Basic dimensions of board
    public static final double PIECERATIO= 0.4; // ration of radius of piece to square size
    public static final int xBOARDpos= 100;   // Position of board
    public static final int yBOARDpos= 100;   // Position of board
    public static final int xMARGIN= 50;   // Position of board
    public static final int yMARGIN= 50;   // Position of board
    public static final int searchDepth= 8;   // Depth of minimax search
    

    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        BoardState initialState= new BoardState();
        initialState.setContents(3, 3, 1);
        initialState.setContents(3, 4, -1);
        initialState.setContents(4, 3, -1);
        initialState.setContents(4, 4, 1);
        initialState.colour= -1;              // Black to start
        
        OthelloDisplay othelloDisplay= new OthelloDisplay();
        othelloDisplay.boardState= initialState;
        othelloDisplay.repaint();
    }
    
    
    
    public static Move chooseMove(BoardState boardState){

        ArrayList<Move> moves= boardState.getLegalMoves();
        if(moves.isEmpty())
            return null;
        // participant version: replace this line with the following code
	    // and provide the routines as directed in the lab exercise script.
        int possibleMove = MIN_VALUE;
        Move nextMoves = null;
        // Iterate through every possible move
        for (Move iterator: moves){
            // Make a move in a separate node
            BoardState nextNode = boardState.deepCopy();
            nextNode.makeLegalMove(iterator.x, iterator.y);
            int currentValue = minimax(nextNode, searchDepth, Integer.MIN_VALUE, Integer.MAX_VALUE);
            // If this move is better than the current move
            if (possibleMove < currentValue ){
                // Change the current best move to the new one found
                possibleMove = currentValue;
                nextMoves = iterator;
            }
        }
        return nextMoves;
        //return moves.get(0);
	/*
        return minimax(boardState, searchDepth);
        */
    }

    public static int[][] valueOnSquare = {
            // Matrix for the importance and value of each square
            {120,-20,20,5,5,20,-20,120},
            {-20,-40,-5,-5,-5,-5,-40,-20},
            {20,-5,15,3,3,15,-5,20},
            {5,-5,3,3,3,3,-5,5},
            {5,-5,3,3,3,3,-5,5},
            {20,-5,15,3,3,15,-5,20},
            {-20,-40,-5,-5,-5,-5,-40,-20},
            {120,-20,20,5,5,20,-20,120},
    };

    public static int staticEvaluationFunction (BoardState Node) {
        // Evaluates the value of the current status of the board
        // And makes a value that shows how good of a position the AI is in
        int value = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                value += valueOnSquare[i][j] * Node.getContents(i, j);
            }
        }
        return value;
    }

    public static int minimax (BoardState Node, int Depth, int alpha, int beta) {
        // Checks what turn it is
        // And the recursively searches for the best position to get to
        if (Depth == 0)
        {
            return staticEvaluationFunction(Node);
        }
        else if (Node.colour == 1)
        {
            alpha = Integer.MIN_VALUE; // Set alpha to -infinite
            int maxLegalMoves = (Node.getLegalMoves()).size();
            int x = 0;

            // If function to check corner case where there a move can't be made
            if (maxLegalMoves == 0)
            {
                BoardState Node_1 = Node.deepCopy();
                Node_1.colour = - Node_1.colour;
                if ((Node_1.getLegalMoves()).size() != 0){
                    return max(alpha, minimax(Node_1, Depth - 1, alpha, beta));
                }
            }

            // This is the recursive loop of the function
            while ((alpha < beta) && (x < maxLegalMoves))
            {
                BoardState Node_1 = Node.deepCopy();
                Move nextMove = Node_1.getLegalMoves().get(x);
                Node_1.makeLegalMove(nextMove.x, nextMove.y);
                alpha = max(alpha, minimax(Node_1, Depth - 1, alpha, beta));
                x += 1;
            }
            return alpha;
        }
        else if (Node.colour == -1)
        {
            beta = Integer.MAX_VALUE; // Set beta to infinite
            int maxLegalMoves = (Node.getLegalMoves()).size();
            int x = 0;

            // If function to check corner case where there a move can't be made
            if (maxLegalMoves == 0)
            {
                BoardState Node_1 = Node.deepCopy();
                Node_1.colour = - Node_1.colour;
                if ((Node_1.getLegalMoves()).size() != 0){
                    return min(beta, minimax(Node_1, Depth - 1, alpha, beta));
                }
            }

            // This is the recursive loop of the function
            while ((alpha < beta) && (x < maxLegalMoves))
            {
                BoardState Node_1 = Node.deepCopy();
                Move nextMove = Node_1.getLegalMoves().get(x);
                Node_1.makeLegalMove(nextMove.x, nextMove.y);
                beta = min(beta, minimax(Node_1, Depth - 1, alpha, beta));
                x += 1;
            }
            return beta;
        }
        return 0;
    }


}
