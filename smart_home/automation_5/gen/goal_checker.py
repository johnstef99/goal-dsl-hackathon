#!/usr/bin/env python3

from goalee import Target, RedisMiddleware
from goalee.topic_goals import TopicMessageReceivedGoal, TopicMessageParamGoal
from goalee.area_goals import RectangleAreaGoal, CircularAreaGoal
from goalee.complex_goal import ComplexGoal, ComplexGoalAlgorithm
from goalee.types import Point


if __name__ == '__main__':
    middleware = RedisMiddleware()
    t = Target(middleware, name='MyAppTarget',
               score_weights=[0.3333333333333333, 0.3333333333333333, 0.3333333333333333])

    g = ComplexGoal(name='Kitchen',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='kitchen.intruder_detected',
                                  name='KitchenIntruder',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    g.add_goal(gs)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='robot.on_enter',
                               name='Kitchen',
                               condition=lambda msg: True if msg['room'] == "kitchen" else False,
                               max_duration=11.0,
                               min_duration=6.0)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='Livingroom',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='livingroom.intruder_detected',
                                  name='LivingroomIntruder',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    g.add_goal(gs)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='robot.on_enter',
                               name='Livingroom',
                               condition=lambda msg: True if msg['room'] == "livingroom" else False,
                               max_duration=10.0,
                               min_duration=5.0)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='Bedroom',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='bedroom.intruder_detected',
                                  name='BedroomIntruder',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    g.add_goal(gs)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='robot.on_enter',
                               name='Bedroom',
                               condition=lambda msg: True if msg['room'] == "bedroom" else False,
                               max_duration=5.0,
                               min_duration=2.0)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_concurrent()
