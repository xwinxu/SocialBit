## Inspiration
Personal data collection is an ever growing trend with smarter and better wearable technology. Already, our sleep, exercise, and food intake can be passively monitored using smartphones, providing valuable insight into our living habits and providing powerful impetus for self-improvement. We wanted develop a technology that adds social interaction to one’s suite of personal data.

## What it does
The SocialBit measures an individual’s social interactions throughout the day. A glasses-mounted camera detects faces and references them with an existing database of the user’s friends on social media platforms. The data is then visualized in a network plot and chord diagram that showcases the length and location of one’s interaction, defined as the points in time in which the friend’s face is within view. The result is a beautiful and insightful display of our daily social interactions - at the microscale.

## How we built it
The Raspberry Pi is designed to be a wearable device that complements your visual senses.
We used a combination of HTML, CSS, Javascript, and D3.js to create our front end and generate our social interaction plots based on output from our computer vision algorithm.
On the back end, we used multiple Python libraries and OpenCV along with the Pi's live stream and fed it into an object detection algorithm that is able to recognize faces, record interaction duration and location, and subsequently record onto a database in real time.

## Challenges we ran into
Getting past internet security while connecting our raspberry pi.
And also Facebook API - every feature we needed was deprecated.

## Accomplishments that we're proud of
We're proud of our concept and for getting most of our backend figured out. 

## What's next for SocialBit
Continuing to refine our technical end, while moving towards integration with other types of personal data. How many steps did you take with your friend? Which friend do you eat more with?
Incentivization is another possibility. Loneliness is a legitimate problem in an increasingly disconnected world - what if our platform could incentivize people to reach their socialization goals, like the FitBit does with exercise?

# Created at HackMIT 2018.
