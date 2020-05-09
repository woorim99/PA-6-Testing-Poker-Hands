import pytest
from card import suits, ranks, Card, PKCard, Deck
from card import Hands

#PKCard 클래스
def test_PKCard_init():
    card = PKCard('AC')
    assert card.rank == 'A' and card.suit == 'C'
    assert card.card == 'AC'

def test_PKCard_init_exception():
    for face in ['10s', 'BD', 'TA']:
        with pytest.raises(ValueError):
            PKCard(face)

def test_PKCard_repr():
    assert repr(PKCard('AC')) == 'AC'


#Hands 클래스
@pytest.fixture
def hand1():     return Hands(['JC', 'TC', '9C', '8C', '7C'])                # straight flush(J)     

@pytest.fixture
def hand2():     return Hands(['5C', '5D', '5S', 'KD', '5C'])                # four of a kind(5)

@pytest.fixture
def hand3():     return Hands(['6S', 'KH', '6D', 'KC', '6H'])                # full house(K)

@pytest.fixture
def hand4():     return Hands(['4D', '9D', '8D', 'KD', '3D'])                # flush(K)

@pytest.fixture
def hand5():     return Hands(['8D', '9S', 'TH', '7D', '6C'])                # straight(T)

@pytest.fixture
def hand6():     return Hands(['QC', '2S', 'QH', '9H', 'QS'])                # three of a kind(Q)

@pytest.fixture
def hand7():     return Hands(['3S', 'JH', '2H', '3C', 'JS'])                # two pair(J, 3)

@pytest.fixture
def hand8():     return Hands(['2S', '2H', '8S', '7H', '4C'])                # one pair(2)

@pytest.fixture
def hand9():     return Hands(['QD', 'KD', '7S', '4S', '3H'])                # high card(K)

@pytest.fixture
def hand10():    return Hands(['4S', 'QH', '3H', '4C', 'QS'])                # two pair(Q,4)

@pytest.fixture
def hand11():    return Hands(['3S', '5H', '3C', '6D', '9S'])                # one pair(3)

@pytest.fixture
def hand12():    return Hands(['3S', 'QD', '4D', 'QC', '3C'])                # two pair(Q,3)

@pytest.fixture
def hand13():    return Hands(['3D', 'QH', '3H', '2C', 'QS'])                # two pair(Q, 3)

@pytest.fixture
def hand14():    return Hands(['3S', '9H', '7S', 'QD', 'JS'])                # high card(Q)

@pytest.fixture
def hand15():    return Hands(['8D', '4D', '6D', '7D', '5D'])                # straight flush(8)

@pytest.fixture
def hand16():    return Hands(['3S', 'QS', '7S', '8S', '4S'])                # flush(Q)

@pytest.fixture
def hand17():    return Hands(['TC', '4D', 'TD', 'TS', 'TH'])                # four of a kind(T)

@pytest.fixture
def hand18():    return Hands(['QS', 'QD', '4C', 'QC', '4H'])                # full house(Q)

@pytest.fixture
def hand19():    return Hands(['6C', '7D', '4H', '5H', '8S'])                # straight(8)

@pytest.fixture
def hand20():    return Hands(['AC', '2D', '2C', 'QD', '2S'])                # three of a kind(2)

@pytest.fixture
def hand21():    return Hands(['3H', '5D', '4H', '3D', '6S'])                # one pair(3)

@pytest.fixture
def hand22():    return Hands(['KH', '4D', '9C', '5C', '3S'])                # high card(K)

def test_is_flush(hand4, hand5):
    assert hand4.is_flush() == True
    assert hand5.is_flush() == False

def test_is_straight(hand5, hand6):
    assert hand5.is_straight() == True
    assert hand6.is_straight() == False

def test_find_a_kind(hand2, hand3, hand6, hand7, hand8):
    assert hand2.find_a_kind() == 'four of a kind'
    assert hand3.find_a_kind() == 'full house'
    assert hand6.find_a_kind() == 'three of a kind'
    assert hand7.find_a_kind() == 'two pair'
    assert hand8.find_a_kind() == 'one pair'

#hand ranking 찾기
def test_tell_hand_ranking(hand1, hand2, hand3, hand4, hand5, hand6, hand7, hand8, hand9):
    assert hand1.tell_hand_ranking() == 'straight flush'
    assert hand2.tell_hand_ranking() == 'four of a kind'
    assert hand3.tell_hand_ranking() == 'full house'
    assert hand4.tell_hand_ranking() == 'flush'
    assert hand5.tell_hand_ranking() == 'straight'
    assert hand6.tell_hand_ranking() == 'three of a kind'
    assert hand7.tell_hand_ranking() == 'two pair'
    assert hand8.tell_hand_ranking() == 'one pair'
    assert hand9.tell_hand_ranking() == 'high card'


#다른 hand ranking끼리 비교
def test_winlose1(hand1, hand2, hand3, hand4, hand5, hand6, hand7, hand8, hand9):
    assert hand1 > hand2                       # testcode = straight flush(J)와 four of a kind(5) 비교
    assert hand3 > hand4                       # testcode = full house(K)와 flush(K) 비교
    assert hand9 < hand5                       # testcode = high card(K)와 straight(T) 비교
    assert hand8 < hand6                       # testcode = one pair(2)와 three of a kind(Q)
    assert hand2 > hand7                       # testcode = four of a kind(5)와 two pair(J, 3) 비교


#같은 hand ranking끼리 비교(find a kind 제외)
def test_winlose2(hand1, hand3, hand4, hand5, hand9, hand14, hand15, hand16, hand18, hand19, hand22):
    assert hand1 > hand15                      # testcode - straight flush(J)와 straight flush(8) 비교
    assert hand4 > hand16                      # testcode - flush(K)와 flush(Q)비교
    assert hand3 > hand18                      # testcode - full house(K)와 full house(Q) 비교
    assert hand5 > hand19                      # testcode - straight(T)와 straight(8)비교
    assert hand9 > hand14                      # testcode - high card(K)와  high card(Q) 비교
    assert hand9 > hand22                      # testcode - high card(K)와 high card(K) 남


#find a kind(one pair, two pair, three of a kind, four of a kind)끼리 비교
def test_winlose3(hand2, hand6, hand7, hand8, hand10, hand11, hand12, hand13, hand17, hand20, hand21):
    assert hand8 < hand11                      # testcode - one pair(2)과 one pair(3) 비교
    assert hand11 > hand21                     # testcode - one pair(3)과 one pair(3) 남은 카드중에 더큰 수를 가진쪽은 hand11
    assert hand7 < hand10                      # testcode - two pair(J,3)과 two pair(Q,4) 비교
    assert hand10 > hand12                     # testcode - two pair(Q,4)와 two pair(Q,3) 비교
    assert hand12 > hand13                     # testcode - two pair(Q,3)와 two pair(Q,3) 비교 남은 카드중에 더큰 수를 가진쪽은 hand12
    assert hand6 > hand20                      # testcode - three of a kind (Q)와 three of a kind(2)비교
    assert hand2 < hand17                      # testcode - four of a kind(5)와 four of a kind(T) 비교




