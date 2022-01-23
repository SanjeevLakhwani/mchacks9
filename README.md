# McHacks 9 Project

Team: Sanjeev Lakhwani, Maxwell Blackburn, Mimi Ohashi Chuapoco

# Dependencies

-   Python 3+

# How to use the project

-   Open `chrome://extensions/`
-   Enable Developer Mode on top right
-   Click on load unpacked and upload the `plugin` from this project

# Devpost

[Devpost Link](https://devpost.com/software/intensorly-distracted)

## Inspiration

Have you found ever yourself trying to learn stuff from youtube and then finding yourself learning more about new cat meme trends for 2022? (We definitely didn't find ourselves in that situation:eyes:). But we've got you covered! Whenever you get distracted, be ready to be intensely stared down by a gif and subject to suspenseful music until you go back to studying.

## What it does

It is a chrome plugin that blocks you from being unproductive on youtube, just like your mom would do when you were a child.

## How we built it

We built a plugin that would get the title of the youtube video you are watching whenever it rendered to the DOM. That title is than ran through our google cloud function which has our own NLP classification model, trained over data that was custom-collected by scraping youtube. Getting the response, depending on what your video is, you can either get shamed for procrastinating or learn more to ace those exams!

## Challenges we ran into

Google Cloud Function is not the best in debugging capabilities-deploying any change to our code took ages.

## Accomplishments that we're proud of

IT WORKS (we think) and was completely made within the time of the hackathon amidst us try attending events within the hackathon. We definitely (well kinda, maybe a little bit) had fun making our project.

## What we learned

You can find awesome teammates, have fun, get Shaq-d, make a useful app, and hate google cloud functions within 36 hours

## What's next for InTensorly Disstrakted

Well it is not just Youtube that might get you DissTrackted, so including supports for other sites such as Facebook, Netflix and other social media platforms. Also, it is fun to watch some fun videos once in a while. Maybe we are wrong sometimes and you do not deserve to get Shaqd! If you wanna educate yourself and your cat about the new cat meme trends for 2022, a "chill mode" might be in order.
