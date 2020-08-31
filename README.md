# EfTIcons

Icons from the game Escape from Tarkov

## Structure

- ```name``` folder contains icons named after their name (no dupelicated files)
- ```uid``` folder contains icons named after their uid (keys and others have are dupelicates)
- ```create.py``` is a script to create the ```uid``` folder from the ```name``` folder
- ```correlation.json``` is used by ```create.py``` to determine the icon to every uid

## Contributing

If you would like to add or update a icon, make sure it fulfills the following criteria:

- Named after its uid / name (check with ```correlation.json```)
- PNG format
- Transparent background
- Width and height (-1) are a multiple of 63. (64x127, 190x442, ...)

![Cotribution example][exampleImg]

## Where to find icons

Rendered icons (moddable items) are cached inside:

```text
C:\Users\User\AppData\Local\Temp\Battlestate Games\EscapeFromTarkov\Icon Cache
```

[exampleImg]: example.png
