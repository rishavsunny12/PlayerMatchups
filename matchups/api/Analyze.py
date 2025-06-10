#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

from groq import Groq


def getSplitStats(content):
    client = Groq(api_key="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",max_retries=3,timeout=60)
    completion = client.chat.completions.create(
        model="compound-beta",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=0.06,
        max_completion_tokens=4000,
        top_p=1,
        stream=False,
        stop=None,
    )



    hitterAnalysis = completion.choices[0].message

    print(hitterAnalysis)
    return hitterAnalysis

def getAnalysisFromLLM(content):
    client = Groq(api_key="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",max_retries=3,timeout=60)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=1,
        max_completion_tokens=5000,
        top_p=1,
        stream=False,
        stop=None,
    )

    Analysis = completion.choices[0].message

   # print(Analysis)
    return Analysis



def analyze(batter,pitcher):

    batterContent = f""" Provide a point-by-point description of {batter} split stats for the current season, including:

1.  **Advanced Metrics**:
    *   OPS (On-Base Plus Slugging)
    *   wOBA (Weighted On-Base Average)
    *   wRC+ (Weighted Runs Created Plus)
    *   BABIP (Batting Average on Balls in Play)
2.  **Stats Against Handedness**:
    *   Batting average vs. left-handed pitchers
    *   On-base percentage vs. left-handed pitchers
    *   Slugging percentage vs. left-handed pitchers
    *   Batting average vs. right-handed pitchers
    *   On-base percentage vs. right-handed pitchers
    *   Slugging percentage vs. right-handed pitchers
3.  **Stats vs. Various Pitch Types**:
    *   Batting average vs. fastballs
    *   On-base percentage vs. fastballs
    *   Slugging percentage vs. fastballs
    *   Batting average vs. breaking balls (e.g., curveballs, sliders)
    *   On-base percentage vs. breaking balls
    *   Slugging percentage vs. breaking balls
    *   Batting average vs. changeups
    *   On-base percentage vs. changeups
    *   Slugging percentage vs. changeups
4.  **Stats vs. Various Pitch Locations**:
    *   Batting average on pitches in the strike zone
    *   On-base percentage on pitches in the strike zone
    *   Slugging percentage on pitches in the strike zone
    *   Batting average on pitches outside the strike zone
    *   On-base percentage on pitches outside the strike zone
    *   Slugging percentage on pitches outside the strike zone

Ensure all information is for the current MLB season and is presented accurately. """
    batterAnalysis = getSplitStats(batterContent)


    pitcherContent = f""" Describe {pitcher} pitching statistics for the current season in a point-by-point format, including the following:

1.  **Basic Performance Metrics:**
    *   Earned Run Average (ERA)
    *   Win-Loss Record
    *   Innings Pitched
    *   Strikeouts
    *   Walks
    *   Hits Allowed

2.  **Advanced Metrics:**
    *   Fielding Independent Pitching (FIP)
    *   Walks and Hits per Inning Pitched (WHIP)
    *   Strikeout-to-Walk Ratio (K/BB)
    *   Opponent Batting Average (OBA)
    *   Home Runs per 9 Innings (HR/9)
    *   BABIP (Batting Average on Balls in Play)

3.  **Performance Against Handedness:**
    *   Batting Average Against Right-Handed Hitters
    *   Batting Average Against Left-Handed Hitters
    *   Strikeout Rate Against Right-Handed Hitters
    *   Strikeout Rate Against Left-Handed Hitters
    *   Walk Rate Against Right-Handed Hitters
    *   Walk Rate Against Left-Handed Hitters
    *   OPS Against Right-Handed Hitters
    *   OPS Against Left-Handed Hitters

4.  **Pitch Types:**
    *   Usage percentage for each pitch type (e.g., fastball, slider, curveball, changeup)
    *   Average velocity for each pitch type
    *   Spin rate for each pitch type
    *   Horizontal and vertical movement for each pitch type
    *   Batting average against each pitch type
    *   Strikeout percentage for each pitch type
    *   Whiff rate for each pitch type

5.  **Pitch Locations:**
    *   Heat maps showing pitch locations in the strike zone
    *   Percentage of pitches thrown in different zones (e.g., high, low, inside, outside)
    *   Batting average against pitches in different zones
    *   Strikeout percentage for pitches in different zones

Ensure the information is well-organized and easy to read. """
    pitcherAnalysis = getSplitStats(pitcherContent)


    finalAnalysisContent = f"""
You will be provided with the following information:

Hitter Stats: {batterAnalysis}
Pitcher Stats: {pitcherAnalysis}

Follow these steps to complete your analysis:

1. Analyze the hitter's stats, focusing on their batting average, on-base percentage, slugging percentage, and any relevant split stats against the type of pitcher they are facing (e.g., left-handed or right-handed).
2. Analyze the pitcher's stats, focusing on their ERA, WHIP, opponent batting average, and any relevant split stats against the type of hitter they are facing (e.g., left-handed or right-handed).
3. Based on your analysis, predict the percentage chance of the hitter getting a hit.
4. Predict the percentage chance of the hitter getting an extra-base hit.
5. Predict the percentage chance of the hitter hitting a home run.
6. Present your predictions in a clear and concise format.

#Follow below format to generate the final analysis always
#output should be easily readable and beautiful to look at

Example Output:
Predicted Outcomes:
Chance of Hit: [XX]%
Chance of Extra-Base Hit: [XX]%
Chance of Home Run: [XX]%

Reasoning(complete analysis here)


"""


    finalAnalysis = getAnalysisFromLLM(finalAnalysisContent)
    print(finalAnalysis)

    return finalAnalysis










