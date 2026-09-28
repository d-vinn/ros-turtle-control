#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "turtlesim/srv/teleport_absolute.hpp"
#include "std_srvs/srv/empty.hpp"

class TurtleBridgeNode : public rclcpp::Node
{
public:
    TurtleBridgeNode() : Node("turtle_bridge_node")
    {
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "/gui_command", 10,
            std::bind(&TurtleBridgeNode::command_callback, this, std::placeholders::_1));

        // 순간이동(절대 위치) 서비스 클라이언트와 리셋 클라이언트 생성
        teleport_client_ = this->create_client<turtlesim::srv::TeleportAbsolute>("/turtle1/teleport_absolute");
        reset_client_ = this->create_client<std_srvs::srv::Empty>("/reset");
    }

private:
    void command_callback(const std_msgs::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Received command: '%s'", msg->data.c_str());

        if (msg->data == "reset") {
            if (reset_client_->wait_for_service(std::chrono::seconds(1))) {
                auto request = std::make_shared<std_srvs::srv::Empty::Request>();
                reset_client_->async_send_request(request);
                // 리셋 시 내부 좌표 기준도 초기화할 수 있도록 관리 가능
                current_x_ = 5.5; current_y_ = 5.5; current_theta_ = 0.0;
            }
            return;
        }

        // 방향에 따른 위치 및 각도 계산
        if (msg->data == "up") {
            current_y_ += 2.0;
            current_theta_ = 1.57; // 위쪽
        } else if (msg->data == "down") {
            current_y_ -= 2.0;
            current_theta_ = -1.57; // 아래쪽
        } else if (msg->data == "right") {
            current_x_ += 2.0;
            current_theta_ = 0.0; // 오른쪽
        } else if (msg->data == "left") {
            current_x_ -= 2.0;
            current_theta_ = 3.14; // 왼쪽
        }

        // Turtlesim에 절대 위치 전송
        if (teleport_client_->wait_for_service(std::chrono::seconds(1))) {
            auto request = std::make_shared<turtlesim::srv::TeleportAbsolute::Request>();
            request->x = current_x_;
            request->y = current_y_;
            request->theta = current_theta_;
            teleport_client_->async_send_request(request);
        }
    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    rclcpp::Client<turtlesim::srv::TeleportAbsolute>::SharedPtr teleport_client_;
    rclcpp::Client<std_srvs::srv::Empty>::SharedPtr reset_client_;

    double current_x_ = 5.5;
    double current_y_ = 5.5;
    double current_theta_ = 0.0;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TurtleBridgeNode>());
    rclcpp::shutdown();
    return 0;
}
