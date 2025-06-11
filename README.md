![image info](images/logo.png)
# Agentowy Chrząszcz Trzcinowy

AI Agents for greater good.

## Use case
### Autonomous Store Optimization
In-store performance is still largely driven by static planning and manual execution—resulting in missed sales, inefficient labor, and poor responsiveness to shopper behavior. Traditional merchandising and pricing systems can't keep up with real-time signals from cameras, sensors, and digital touchpoints. This use case introduces a multi-agent system that coordinates across pricing, layout, inventory, and labor management to dynamically adapt the store environment based on live inputs—maximizing conversion and customer satisfaction while minimizing operational waste.
#### Parameters
- Monitor foot traffic, POS, and Wi-Fi data to detect demand shifts in real time.
- Adjust product displays, signage, and screen content based on traffic patterns.
- Reposition underperforming products based on consumer engagement.
- Dynamically update digital shelf labels and prices to match competitors.
- Launch targeted promotions based on time, inventory, and sales performance.
- Detect low-shelf stock using cameras or sensors and trigger restocking tasks.
- Reassign staff based on queue length, traffic surges, and replenishment urgency.
- Coordinate with robotic shelving or push layout guidance to mobile devices.
- Deliver AI concierge experiences via smart displays and mobile apps.
- Personalize product suggestions and offers based on loyalty behavior.

## Ideas
Usability based shop management system based on AI Agents. Except standard food store (whatever size it is) stuff system is focused on giving solutions like recipes with list of products which are currently available in the shop. Or advices that i'll warm next few days and there are suitable products in the shop.

## Components
System is built on:
- network of devices (shelf occupancy counters, shelf labels, cameras with traffic information, cash registers, screens, ...),
- event queue,
- network of agents,
- enduser devices (shop employees, customers, shop robots and so on).

## Agents
### LLM
- Recipe Agent - bierze zalegające produkty, szuka przepisów, w których można je wykorzystać, sprawdza czy w sklepie są pozostałe potrzebne produkty, wybiera najlepusze przepisy i wysyła do Agenta Reklamiarza
- Planner Agent - bierze prognozę pogody od agenta Synoptyka, sprawdza co będzie się dobrze sprzedawało i wysyła listę do agenta Zaopatrzeniowca
- Marketing Agent - preparation of materials to be displayed on screens (i.e. recipe with picture, list of products with locations in the shop, recipe itself and QR-code linking to webpage with details).

### Tool
- kasa, półka, magazyn, ludzie,
- Agent Półkowy - wysyła zlecenia uzupełnienia stanu na półce