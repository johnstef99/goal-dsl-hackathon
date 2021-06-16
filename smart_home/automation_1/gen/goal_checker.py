#!/usr/bin/env python3

from goalee import Target, RedisMiddleware
from goalee.topic_goals import TopicMessageReceivedGoal, TopicMessageParamGoal
from goalee.area_goals import RectangleAreaGoal, CircularAreaGoal
from goalee.complex_goal import ComplexGoal, ComplexGoalAlgorithm
from goalee.types import Point


if __name__ == '__main__':
    middleware = RedisMiddleware()
    t = Target(middleware, name='MyAppTarget',
               score_weights=[1.0])

    g = ComplexGoal(name='Main',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='kitchen.gas',
                               name='GasTrigger',
                               condition=lambda msg: True if msg['gas'] > 0.3 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_concurrent()
