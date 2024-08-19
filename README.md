<br />
<div align="left">
  <h1>The highlights of my python projects</h1>
  <!--intro paragraph -->
  <p>In this repository, I have collected some of the coolest python projects I have done during the coding studies:</p>
  <ul>
    <li>
      <a href="#robojump">RoboJump 3000 - a platform game made with Python's Pygame module</a>
    </li>
    <li>
      <a href="#radialfade">Radial fade filter for an image</a>
    </li>
    <li>
      <a href=#probabilistic">A probabilistic research on high blood pressure and coronary artery disease (linear and logistic regression)</a>  
    </li>  
  </ul>
</div>
<hr>

<!-- Robojump -->
<h3 id="robojump">RoboJump 3000</h3>  
<!-- Robojump screen cap -->
![image](https://github.com/user-attachments/assets/f7a3ef32-4f99-4c6f-8a43-d7c74293b82e)

<!-- Robojump description -->
<div>
  <p>RoboJump 3000 is a classic platformer game where the player controls a robot that needs to jump from one platform to another to stay in the game. The goal is to collect as many coins as possible. The difficulty increases incrementally due to the presence of ghosts (known as "mörkö") and the increasing speed of the platforms. This game project was a part of course called "Python programming MOOC" offered by Helsinki University. 
  </p>
  <p>The animation of the game was created with a Python module called <a href="https://en.wikipedia.org/wiki/Pygame">Pygame</a>. The logic in the code is the following:
    <ul>
      <li>The platforms, coins, and ghosts are represented as groups of images, with their coordinates defined in a dictionary.</li>  
      <li>All elements (except for the robot) move downward at a predefined speed, which increases incrementally and makes it harder to stay in the game.</li>
      <li>A while loop updates the coordinates of these elements in each iteration. It also checks if the robot is moving, if it collects a coin or encounters a ghost, or if it falls out of the game.</li>
    </ul>
  </p>
</div>

<hr>
<!-- Radial fade description -->
<h3 id="radialfade">Radial fade filter for an image</h3>
<!-- Radial fade image -->
<img width="265" alt="image" src="https://github.com/user-attachments/assets/4a3036cf-b2b9-4ec5-a871-cd56c3f45633">

<!-- Radial fade description -->
<div>
  <p>A radial fade filter applies a fading effect to a black-and-white (1-D) or color (3-D) image in a radial direction. In other words, as we move away from the center of the image, the pixels gradually fade to black. The first image in the screen capture is the original image, the second is the fading mask, and the third is the filtered image. This filter was part of a programming course called "Data Analysis with Python," offered by Helsinki University.
  </p>
  <p>The filter was written in Python, and the logic of the code is as follows:
    <ul>
      <li>A mask array is created for the image, where each value represents the radial distance from the center, scaled to the range of 0 to 1. The first and the second dimensions correspond to the height and width of each pixel respectively.</li>  
      <li>The values in the mask array are then inverted, so that values closer to the center are near 1, and the values further from the center close to 0.</li>
      <li>The third dimension of the mask array is expanded to 3-D to be compatible with RGB images. Finally, the mask array is multiplied with the original image to apply the fade effect.</li>
    </ul>
  </p>
</div>

<hr>
<!-- Linear and logistic regression project -->
<h3 id="probabilistic">A probabilistic research on high blood pressure and coronary artery disease (linear and logistic regression)</h3>
<!-- Linear and logistic regression project image -->

<!-- Linear and logistic regression project description -->



