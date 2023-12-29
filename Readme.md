-- under construction


## Domains (Entities)
- Dealer
  Entity is used to control game flow (serve cards, etc)

- Board
  Gaming board
  holds also information that are accessable for players (like open cards)

- Players
  Play the game
  Subclasses: smart player and random player

- Cards
  Cards deck;
  Subclasses: cards offset and cards open
